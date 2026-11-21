# 1-Click Sync & Push to GitHub with Sanitization
param(
    [switch]$Push = $false
)

$repoDir = "C:\Projects\enterprise-agent-skills"
$pyScript = "$repoDir\scripts\sync_and_sanitize.py"

if ($Push) {
    python $pyScript --push
} else {
    python $pyScript
}
