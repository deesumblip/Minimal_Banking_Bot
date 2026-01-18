$ErrorActionPreference = "Stop"

# Usage: . .\load_env.ps1
# Loads environment variables from .env into the current PowerShell session

if (-not (Test-Path ".env")) { throw ".env not found in this folder." }

Get-Content ".env" | ForEach-Object {
  $line = $_.Trim()
  if (-not $line -or $line.StartsWith("#")) { return }
  $k, $v = $line.Split("=", 2)
  if ($k) { Set-Item -Path "Env:$($k.Trim())" -Value $v.Trim().Trim('"') }
}

# Require RASA_LICENSE
if (-not $env:RASA_LICENSE) { throw "RASA_LICENSE not found in .env file." }
