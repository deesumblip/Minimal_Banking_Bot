# Start Level 6 with DEBUG logs: MCP + action server + rasa inspect (background).
# Logs under level6/logs/ with a timestamp. Inspector URL printed at end.
#
# Usage (from repo root):
#   powershell -ExecutionPolicy Bypass -File level6/scripts/run-stack-inspector-debug.ps1
#
# Stop: Task Manager or: Get-NetTCPConnection -LocalPort 8080,5055,5005 | % { Stop-Process -Id $_.OwningProcess -Force }

$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$lv6 = Resolve-Path (Join-Path $PSScriptRoot "..")
$py = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) { Write-Error "Missing venv: $py" }

$logDir = Join-Path $lv6 "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"

Get-NetTCPConnection -LocalPort 8080,5005,5055 -ErrorAction SilentlyContinue |
    ForEach-Object { $_.OwningProcess } | Sort-Object -Unique |
    ForEach-Object { Stop-Process -Id $_ -Force -ErrorAction SilentlyContinue }
Start-Sleep -Seconds 2

$mcpOut = Join-Path $logDir "mcp-debug-$stamp.log"
$mcpErr = Join-Path $logDir "mcp-debug-$stamp.err.log"
$actOut = Join-Path $logDir "actions-debug-$stamp.log"
$actErr = Join-Path $logDir "actions-debug-$stamp.err.log"
$rasaLog = Join-Path $logDir "inspect-rasa-debug-$stamp.log"
$insOut = Join-Path $logDir "inspect-console-$stamp.log"
$insErr = Join-Path $logDir "inspect-console-$stamp.err.log"

Start-Process -FilePath $py -ArgumentList "mcp_server/banking.py" -WorkingDirectory $lv6 `
    -WindowStyle Hidden -RedirectStandardOutput $mcpOut -RedirectStandardError $mcpErr -PassThru | Out-Null
Start-Sleep -Seconds 4

Start-Process -FilePath $py -ArgumentList "-m","rasa","run","actions","-vv" -WorkingDirectory $lv6 `
    -WindowStyle Hidden -RedirectStandardOutput $actOut -RedirectStandardError $actErr -PassThru | Out-Null
Start-Sleep -Seconds 6

Start-Process -FilePath $py -ArgumentList "-m","rasa","inspect","-vv","--log-file",$rasaLog -WorkingDirectory $lv6 `
    -WindowStyle Hidden -RedirectStandardOutput $insOut -RedirectStandardError $insErr -PassThru | Out-Null

Write-Host "DEBUG logs (stamp $stamp):" -ForegroundColor Cyan
Write-Host "  MCP:           $mcpOut"
Write-Host "  MCP stderr:    $mcpErr"
Write-Host "  Actions:       $actOut / $actErr"
Write-Host "  Inspect Rasa:  $rasaLog  (--log-file)"
Write-Host "  Inspect proc:  $insOut / $insErr"
Write-Host ""
Write-Host "Inspector: http://localhost:5005/webhooks/socketio/inspect.html" -ForegroundColor Green
Write-Host "Wait ~30s for Rasa to load, then open the URL." -ForegroundColor Yellow
