# Level 6: Run Rasa Inspector (chat UI)
#
# Prerequisites (separate terminals, venv active, cd level6):
#   1. python mcp_server/banking.py
#   2. python -m rasa run actions
#
# Then from level6:
#   powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
#
# Open in browser:
#   http://localhost:5005/webhooks/socketio/inspect.html
# (If port 5005 is busy, add: -p 5025 and use that port in the URL.)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonExe = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    Write-Error "Expected venv at $pythonExe"
}

New-Item -ItemType Directory -Force -Path (Join-Path $PSScriptRoot "logs") | Out-Null
$logFile = Join-Path $PSScriptRoot "logs\inspect.log"

Write-Host "Starting Rasa Inspector (DEBUG) on http://127.0.0.1:5005" -ForegroundColor Cyan
Write-Host "Open: http://localhost:5005/webhooks/socketio/inspect.html" -ForegroundColor Green
Write-Host "Debug log file: $logFile" -ForegroundColor Gray
Write-Host "Press Ctrl+C to stop." -ForegroundColor Yellow
# -vv = DEBUG logging (same as --debug in Rasa CLI)
& $pythonExe -m rasa inspect -vv --log-file $logFile
exit $LASTEXITCODE
