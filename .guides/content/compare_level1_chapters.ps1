# Compare Level-1-1-d3b4 vs Chapter-1-1---Just-Responses-d3b4 (Units 0-3 overlap).
# Run from repo root: .\.guides\content\compare_level1_chapters.ps1

$Level  = ".guides/content/Level-1-1-d3b4"
$Chapter = ".guides/content/Chapter-1-1---Just-Responses-d3b4"

if (-not (Test-Path $Level)) {
    Write-Host "Level-1-1-d3b4 not found at $Level"
    exit 1
}
if (-not (Test-Path $Chapter)) {
    Write-Host "Chapter-1-1---Just-Responses-d3b4 not found at $Chapter"
    Write-Host "Copy it from Codio into the repo to compare."
    exit 1
}

Write-Host "=== Level-1-1-d3b4 (repo) - Units 0-3 ==="
Get-ChildItem -Path $Level -Recurse -Filter "*.md" | ForEach-Object {
    $rel = $_.FullName.Replace((Resolve-Path $Level).Path + [IO.Path]::DirectorySeparatorChar, "")
    Write-Host "  $rel"
}

Write-Host ""
Write-Host "=== Chapter-1-1---Just-Responses-d3b4 - Units 0-3 ==="
Get-ChildItem -Path $Chapter -Recurse -Filter "*.md" | Where-Object {
    $rel = $_.FullName.Replace((Resolve-Path $Chapter).Path + [IO.Path]::DirectorySeparatorChar, "")
    $rel -match "^Unit-[0-3]"
} | ForEach-Object {
    $rel = $_.FullName.Replace((Resolve-Path $Chapter).Path + [IO.Path]::DirectorySeparatorChar, "")
    Write-Host "  $rel"
}

Write-Host ""
Write-Host "=== Comparing by filename (same .md name in any Unit-0..3 folder) ==="
$levelFiles = Get-ChildItem -Path $Level -Recurse -Filter "*.md" | ForEach-Object { $_.Name }
$chapterFiles = Get-ChildItem -Path $Chapter -Recurse -Filter "*.md" | Where-Object {
    $_.FullName -match "Unit-[0-3]"
} | ForEach-Object { $_.Name }

$common = $levelFiles | Where-Object { $_ -in $chapterFiles }
$onlyInLevel = $levelFiles | Where-Object { $_ -notin $chapterFiles }
$onlyInChapter = $chapterFiles | Where-Object { $_ -notin $levelFiles }

Write-Host "  Files with same name in both: $($common.Count)"
$common | ForEach-Object { Write-Host "    $_" }
Write-Host "  Only in Level-1-1-d3b4: $($onlyInLevel.Count)"
$onlyInLevel | ForEach-Object { Write-Host "    $_" }
Write-Host "  Only in Chapter-1-1 (Units 0-3): $($onlyInChapter.Count)"
$onlyInChapter | ForEach-Object { Write-Host "    $_" }

Write-Host ""
Write-Host "To diff a specific file, run:"
Write-Host '  diff (Get-Content ".guides/content/Level-1-1-d3b4/Unit-0--.../file.md") (Get-Content ".guides/content/Chapter-1-1---Just-Responses-d3b4/Unit-0-.../file.md")'
