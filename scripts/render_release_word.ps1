# Native Word fallback after the bundled renderer reports missing soffice.exe.
# Read-only input, hidden dedicated automation instance, no manuscript mutation.
$ErrorActionPreference = 'Stop'
$releaseRoot = Split-Path -Parent $PSScriptRoot
$releaseOutput = Join-Path $releaseRoot 'tmp\stage20\docx'
New-Item -ItemType Directory -Force $releaseOutput | Out-Null
$releaseWord = New-Object -ComObject Word.Application
$releaseWord.Visible = $false
$releaseWord.DisplayAlerts = 0
try {
    $releaseDoc = $releaseWord.Documents.Open((Join-Path $releaseRoot 'output\release\Constrained-Annealing-2026.docx'), $false, $true)
    $releaseDoc.Fields.Update() | Out-Null
    $releaseDoc.ExportAsFixedFormat((Join-Path $releaseOutput 'word-render.pdf'), 17)
    $releaseDoc.Close(0)
} finally {
    $releaseWord.Quit()
}
