# Level 5: Train + Run Inspector
# From level5/:
#   powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
# Uses the shared .venv at repo root (Minimal_Banking_Bot/.venv).

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonExe = Join-Path $repoRoot ".venv\Scripts\python.exe"

Write-Host "== Level 5: Train + Run Inspector ==" -ForegroundColor Cyan

Write-Host "Loading environment variables from .env..." -ForegroundColor Gray
. .\load_env.ps1

Write-Host "Ensuring logs/ folder exists..." -ForegroundColor Gray
New-Item -ItemType Directory -Force logs | Out-Null

Write-Host "Training (rasa train)..." -ForegroundColor Gray
& $pythonExe -m rasa train
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Starting Inspector on http://localhost:5005/webhooks/socketio/inspect.html" -ForegroundColor Green
Write-Host "Press Ctrl+C in this window to stop." -ForegroundColor Yellow
& $pythonExe -m rasa inspect --debug --log-file logs/logs.out
exit $LASTEXITCODE
