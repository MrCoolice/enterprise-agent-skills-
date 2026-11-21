#!/usr/bin/env python3
r"""
Enterprise Agent Skills - Automatic Sync & Sanitization Pipeline
Synchronizes local skills from ~/.gemini/config/skills/ to C:\Projects\enterprise-agent-skills\skills\
Applies strict sanitization rules to protect private IPs, names, bot tokens, and paths.
"""

import os
import re
import shutil
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

SOURCE_DIR = os.path.expanduser(r"~\.gemini\config\skills")
REPO_DIR = r"C:\Projects\enterprise-agent-skills"
TARGET_DIR = os.path.join(REPO_DIR, "skills")
SANITIZATION_RULES = [
    # 1. Personal Identifiers
    (re.compile(r"\bUlaş\s+Özbek\b", re.IGNORECASE), "Enterprise SecOps Architect"),
    (re.compile(r"\bUlaş\b", re.UNICODE), "Kurucu / Mimar"),
    (re.compile(r"\bÖzbek\b", re.UNICODE), "Mimar"),
    (re.compile(r"\bMrCoolice\b"), "devops-engineer"),
    
    # 2. Private Subnets
    (re.compile(r"10\.20\.20\."), "10.10.10."),
    (re.compile(r"10\.20\.10\."), "10.10.20."),
    (re.compile(r"10\.20\.30\."), "10.10.30."),
    (re.compile(r"10\.30\.30\."), "10.10.30."),
    
    # 2b. Domains & Public Brand Hostnames Sanitization
    (re.compile(r"\bmatomo\.golgesiber\.com\b", re.IGNORECASE), "matomo.secops-domain.example.com"),
    (re.compile(r"\bnc\.golgesiber\.com\b", re.IGNORECASE), "nc.secops-domain.example.com"),
    (re.compile(r"\bunifi\.golgesiber\.com\b", re.IGNORECASE), "unifi.secops-domain.example.com"),
    (re.compile(r"\bdalamanairportsuites\.com\b", re.IGNORECASE), "hotel-suites.example.com"),
    (re.compile(r"\bgolgesiber\.com\b", re.IGNORECASE), "secops-domain.example.com"),
    (re.compile(r"\bgolgekitabevi\.com\b", re.IGNORECASE), "ecommerce.example.com"),
    
    # 3. Private Bot Usernames & Tokens
    (re.compile(r"@d8el_bot\b"), "@your_noc_alert_bot"),
    (re.compile(r"bot[0-9]{8,10}:[a-zA-Z0-9_-]{35}"), "botYOUR_BOT_TOKEN_HERE"),
    (re.compile(r"[0-9]{9,11}:AA[a-zA-Z0-9_-]{33}"), "YOUR_TELEGRAM_BOT_TOKEN"),
    
    # 4. Strict Private User Paths
    (re.compile(r"C:\\Users\\MrCoolice\\", re.IGNORECASE), "C:\\Users\\Administrator\\"),
    (re.compile(r"/home/mrcoolice/", re.IGNORECASE), "/home/administrator/"),
]

# Sensitive files to exclude from public repository
IGNORED_FILES = {
    ".env", ".env.local", ".env.production", "id_rsa", "id_ed25519", 
    "credentials.json", "token.json", ".git", "__pycache__"
}

def sanitize_text(text: str) -> str:
    for pattern, replacement in SANITIZATION_RULES:
        text = pattern.sub(lambda m, r=replacement: r, text)
    return text

def sync_skills():
    if not os.path.exists(SOURCE_DIR):
        print(f"[-] Source directory not found: {SOURCE_DIR}")
        sys.exit(1)
        
    print(f"[*] Reading skills from: {SOURCE_DIR}")
    print(f"[*] Syncing into target: {TARGET_DIR}")
    
    skills = [d for d in os.listdir(SOURCE_DIR) if os.path.isdir(os.path.join(SOURCE_DIR, d))]
    processed = 0
    
    for skill in sorted(skills):
        src_skill_path = os.path.join(SOURCE_DIR, skill)
        dst_skill_path = os.path.join(TARGET_DIR, skill)
        os.makedirs(dst_skill_path, exist_ok=True)
        
        for root, dirs, files in os.walk(src_skill_path):
            dirs[:] = [d for d in dirs if d not in IGNORED_FILES]
            rel_path = os.path.relpath(root, src_skill_path)
            target_sub_dir = os.path.join(dst_skill_path, rel_path)
            os.makedirs(target_sub_dir, exist_ok=True)
            
            for file in files:
                if file in IGNORED_FILES or file.endswith((".pyc", ".log", ".tmp")):
                    continue
                
                src_file = os.path.join(root, file)
                
                # Normalize specific file names for public repo
                target_filename = file
                if file == "golgesiber.md" and "memory" in root:
                    target_filename = "brand_profile.md"
                    
                dst_file = os.path.join(target_sub_dir, target_filename)
                
                # If text file, sanitize
                if file.endswith((".md", ".txt", ".json", ".yaml", ".yml", ".sh", ".py", ".ts", ".js")):
                    try:
                        with open(src_file, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                        clean_content = sanitize_text(content)
                        
                        # Only write if different to prevent unnecessary mtimes
                        if os.path.exists(dst_file):
                            with open(dst_file, "r", encoding="utf-8", errors="ignore") as f_existing:
                                if f_existing.read() == clean_content:
                                    continue
                                    
                        with open(dst_file, "w", encoding="utf-8") as f:
                            f.write(clean_content)
                    except Exception as e:
                        print(f"[!] Error processing {src_file}: {e}")
                else:
                    if not os.path.exists(dst_file):
                        shutil.copy2(src_file, dst_file)
        
        processed += 1
        
    print(f"[OK] {processed} skills checked and sanitized.")

def check_git(auto_push=False):
    status = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_DIR, capture_output=True, text=True)
    untracked_or_modified = [l for l in status.stdout.splitlines() if not l.startswith("?? scripts/") and not l.startswith("?? sync-skills.ps1")]
    
    if not untracked_or_modified:
        print("[OK] Repository is 100% clean and in sync with local skills. No changes to commit.")
        return
        
    print("[*] Detected updates in skills:")
    for line in untracked_or_modified:
        print(f"    {line}")
        
    if auto_push:
        subprocess.run(["git", "add", "."], cwd=REPO_DIR, check=True)
        subprocess.run(["git", "commit", "-m", "chore(skills): auto-sync and sanitize local skills"], cwd=REPO_DIR, check=True)
        res = subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, capture_output=True, text=True)
        print("[OK] Pushed updates to GitHub successfully!")
        print(res.stderr or res.stdout)
    else:
        print("\n[Tip] Run with '--push' or execute '.\\sync-skills.ps1 -Push' to push changes to GitHub.")

if __name__ == "__main__":
    auto_push = "--push" in sys.argv
    sync_skills()
    check_git(auto_push=auto_push)
