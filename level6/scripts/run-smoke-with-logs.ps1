# Level 6: start MCP + action server + Rasa, probe HTTP, write timestamped logs under ../logs/
# Usage:
#   powershell -ExecutionPolicy Bypass -File level6/scripts/run-smoke-with-logs.ps1
# If port 5005 is busy: -RasaPort 5006
# Leave servers running: -SkipStop

param(
    [int] $RasaPort = 5005,
    [switch] $SkipStop
)

$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$py = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    Write-Error "Expected venv at $py. Activate .venv from Minimal_Banking_Bot checkout."
}
$lv6 = Resolve-Path (Join-Path $PSScriptRoot "..")

$logDir = Join-Path $lv6 "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"

$metaPath = Join-Path $logDir ("smoke-{0}.meta.txt" -f $stamp)
$metaText = @"
=== Level 6 smoke $stamp ===
RASA_LICENSE env set: $([bool]$env:RASA_LICENSE)
RasaPort: $RasaPort
WorkingDirectory: $lv6
Python: $py
"@
$metaText | Set-Content -Encoding utf8 $metaPath

function Start-BgProcess {
    param(
        [string[]] $ArgumentList,
        [string] $StdOutPath,
        [string] $StdErrPath
    )
    return (Start-Process -FilePath $py -ArgumentList $ArgumentList -WorkingDirectory $lv6 -PassThru -WindowStyle Hidden `
        -RedirectStandardOutput $StdOutPath -RedirectStandardError $StdErrPath)
}

$mcpOut = Join-Path $logDir ("mcp-{0}.log" -f $stamp)
$mcpErr = Join-Path $logDir ("mcp-{0}.err.log" -f $stamp)
$pMcp = Start-BgProcess -ArgumentList @("mcp_server/banking.py") -StdOutPath $mcpOut -StdErrPath $mcpErr
Start-Sleep -Seconds 4

$actOut = Join-Path $logDir ("actions-{0}.log" -f $stamp)
$actErr = Join-Path $logDir ("actions-{0}.err.log" -f $stamp)
$pAct = Start-BgProcess -ArgumentList @("-m", "rasa", "run", "actions") -StdOutPath $actOut -StdErrPath $actErr
Start-Sleep -Seconds 6

$rasOut = Join-Path $logDir ("rasa-{0}.log" -f $stamp)
$rasErr = Join-Path $logDir ("rasa-{0}.err.log" -f $stamp)
$pRasa = Start-BgProcess -ArgumentList @("-m", "rasa", "run", "--enable-api", "--debug", "-p", "$RasaPort") -StdOutPath $rasOut -StdErrPath $rasErr
Start-Sleep -Seconds 28

$base = "http://127.0.0.1:$RasaPort"
$sumPath = Join-Path $logDir ("smoke-{0}.summary.txt" -f $stamp)
$lines = New-Object System.Collections.Generic.List[string]

try {
    $v = Invoke-RestMethod -Uri "$base/version" -TimeoutSec 15
    $lines.Add("version OK: " + ($v | ConvertTo-Json -Compress))
} catch {
    $lines.Add("version FAIL: " + $_.Exception.Message)
}

try {
    $s = Invoke-RestMethod -Uri "$base/status" -TimeoutSec 15
    $lines.Add("status OK: " + ($s | ConvertTo-Json -Compress))
} catch {
    $lines.Add("status FAIL: " + $_.Exception.Message)
}

$body = '{"sender":"smoke-test","message":"hi"}'
try {
    $r = Invoke-RestMethod -Uri "$base/webhooks/rest/webhook" -Method Post -Body $body -ContentType "application/json" -TimeoutSec 60
    $lines.Add("webhook hi OK: " + ($r | ConvertTo-Json -Compress -Depth 6))
} catch {
    $lines.Add("webhook hi FAIL: " + $_.Exception.Message)
}

$lines.Add("PIDs: MCP=$($pMcp.Id) Actions=$($pAct.Id) Rasa=$($pRasa.Id)")
$lines | Set-Content -Encoding utf8 $sumPath
Get-Content $sumPath

if (-not $SkipStop) {
    Stop-Process -Id $pRasa.Id -Force -ErrorAction SilentlyContinue
    Stop-Process -Id $pAct.Id -Force -ErrorAction SilentlyContinue
    Stop-Process -Id $pMcp.Id -Force -ErrorAction SilentlyContinue
    "Stopped PIDs." | Add-Content -Encoding utf8 $sumPath
}

Write-Host "Logs: $logDir (stamp $stamp)"
