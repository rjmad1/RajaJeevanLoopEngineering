# interactive-bootstrap.ps1
#
# Interactive CLI utility to initialize the Conductor Loop Engineering Framework in any project.
# Prompts for target project path and type, executes port-loops.ps1, and displays setup instructions.

$ErrorActionPreference = "Stop"

Clear-Host

Write-Host "==========================================================" -ForegroundColor Green
Write-Host "     RAJA JEEVAN - LOOP ENGINEERING BOOTSTRAP UTILITY     " -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
Write-Host ""
Write-Host "This utility configures structured AI agent execution loops and"
Write-Host "Dev Container workspace settings in any target repository."
Write-Host ""

# 1. Prompt for Project Location
$ValidPath = $false
$TargetDir = ""

while (-not $ValidPath) {
    $InputPath = Read-Host "Enter the absolute local path to your target project folder"
    if ([string]::IsNullOrWhiteSpace($InputPath)) {
        Write-Host "Error: Path cannot be empty." -ForegroundColor Red
        continue
    }

    # Resolve relative paths or home paths if needed
    $ResolvedPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($InputPath)

    if (-not (Test-Path -Path $ResolvedPath)) {
        Write-Host "Directory does not exist: $ResolvedPath" -ForegroundColor Yellow
        $CreateChoice = Read-Host "Do you want to create this directory? (Y/N)"
        if ($CreateChoice -eq 'Y' -or $CreateChoice -eq 'y') {
            try {
                New-Item -ItemType Directory -Force -Path $ResolvedPath | Out-Null
                $TargetDir = $ResolvedPath
                $ValidPath = $true
            } catch {
                Write-Host "Error creating directory: $_" -ForegroundColor Red
            }
        }
    } else {
        $TargetDir = $ResolvedPath
        $ValidPath = $true
    }
}

# 2. Prompt for Project Type
Write-Host ""
Write-Host "Select the nature of your target project:" -ForegroundColor Green
Write-Host "  [1] Greenfield        - Architecture ADR design, Spec Authoring, Test Setup, Initial Code Gen."
Write-Host "  [2] Brownfield        - Context Assembly, Regression Tests, Safe Mod, verification, refactoring."
Write-Host "  [3] Modernization     - System Discovery, Code Review, Decoupling, API Contract validation."
Write-Host "  [4] Incident Response - RCA, Reproduction Tests, Hotfixing, Verification, Post-Mortem Reflection."
Write-Host "  [5] All Loops         - Installs the entire loop catalog suite."
Write-Host ""

$ValidChoice = $false
$ProjectType = ""

while (-not $ValidChoice) {
    $ChoiceInput = Read-Host "Select Project Type [1-5]"
    switch ($ChoiceInput) {
        "1" { $ProjectType = "Greenfield"; $ValidChoice = $true }
        "2" { $ProjectType = "Brownfield"; $ValidChoice = $true }
        "3" { $ProjectType = "Modernization"; $ValidChoice = $true }
        "4" { $ProjectType = "IncidentResponse"; $ValidChoice = $true }
        "5" { $ProjectType = "All"; $ValidChoice = $true }
        default { Write-Host "Invalid choice. Please select a number between 1 and 5." -ForegroundColor Red }
    }
}

Write-Host ""
Write-Host "Starting loop provisioning..." -ForegroundColor Yellow

# Locate port-loops.ps1 relative to this script
$PortScript = Join-Path $PSScriptRoot "port-loops.ps1"
if (-not (Test-Path $PortScript)) {
    # Fallback to local execution directory if running ad-hoc
    $PortScript = Join-Path (Get-Location) "port-loops.ps1"
}

if (-not (Test-Path $PortScript)) {
    Write-Error "Could not find 'port-loops.ps1' at: $PortScript"
    exit 1
}

# Execute the porting logic
try {
    & $PortScript -TargetProjectPath $TargetDir -ProjectType $ProjectType -OverwriteDevContainer
} catch {
    Write-Host "Failed to provision loops: $_" -ForegroundColor Red
    exit 1
}
