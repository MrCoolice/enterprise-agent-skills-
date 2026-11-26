#!/usr/bin/env python3
"""
Audiophile Music Curator - Dynamic Library Configuration & Discovery
Resolves the active music library directory dynamically without hardcoded usernames or paths.
"""
import os
import json

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")


def get_library_dir() -> str:
    """
    Returns the active music library directory using a 4-tier discovery order:
    1. Environment variable: AUDIOPHILE_MUSIC_DIR or CORSA_MUSIC_DIR
    2. config.json: previously saved user preference
    3. Auto-detection:
       - ~/Nextcloud/Music (if Nextcloud is used)
       - ~/Music/Corsa-Library
       - ~/Music (OS default Music directory)
    4. Fallback: ~/Music
    """
    # 1. Environment variable
    env_dir = os.environ.get("AUDIOPHILE_MUSIC_DIR") or os.environ.get("CORSA_MUSIC_DIR")
    if env_dir:
        env_dir = os.path.abspath(os.path.expanduser(env_dir))
        if os.path.isdir(env_dir):
            return env_dir

    # 2. config.json
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                cfg_dir = cfg.get("library_dir")
                if cfg_dir:
                    cfg_dir = os.path.abspath(os.path.expanduser(cfg_dir))
                    if os.path.isdir(cfg_dir):
                        return cfg_dir
        except Exception:
            pass

    # 3. Auto-detection
    home = os.path.expanduser("~")
    candidates = [
        os.path.join(home, "Nextcloud", "Music"),
        os.path.join(home, "Music", "Corsa-Library"),
        os.path.join(home, "Music"),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return os.path.abspath(c)

    # 4. Fallback default
    fallback = os.path.join(home, "Music")
    os.makedirs(fallback, exist_ok=True)
    return os.path.abspath(fallback)


def set_library_dir(new_path: str) -> str:
    """Saves the user-selected music directory to config.json."""
    abs_path = os.path.abspath(os.path.expanduser(new_path.strip('"').strip("'")))
    os.makedirs(abs_path, exist_ok=True)
    cfg = {}
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception:
            pass
    cfg["library_dir"] = abs_path
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    return abs_path
