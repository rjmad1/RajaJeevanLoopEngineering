# port-loops.ps1
#
# Ports the Conductor Loop Engineering Framework to target projects.
# Sets up loop documents, templates, rule engines, and dev container configurations.
#
# Usage:
#   .\port-loops.ps1 -TargetProjectPath "C:\Users\rajaj\Projects\customer-billing-service" -ProjectType "Brownfield"

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true, HelpMessage="Absolute path to the target repository/project")]
    [string]$TargetProjectPath,

    [Parameter(Mandatory=$true, HelpMessage="Nature of the project determining loop selection")]
    [ValidateSet("Greenfield", "Brownfield", "Modernization", "IncidentResponse", "All")]
    [string]$ProjectType,

    [Parameter(Mandatory=$false)]
    [switch]$OverwriteDevContainer
)

# Set strict execution controls
$ErrorActionPreference = "Stop"

# Source Library Root is local to where the script runs
$SrcLibRoot = $PSScriptRoot
if ([string]::IsNullOrEmpty($SrcLibRoot)) {
    $SrcLibRoot = Get-Location
}

Write-Host "=== Conductor Loop Engineering Porting Utility ===" -ForegroundColor Green
Write-Host "Source Library: $SrcLibRoot" -ForegroundColor Gray
Write-Host "Target Project: $TargetProjectPath" -ForegroundColor Gray
Write-Host "Project Type  : $ProjectType" -ForegroundColor Gray
Write-Host ""

# 1. Path Validations
if (-not (Test-Path -Path $TargetProjectPath)) {
    Write-Host "Target path does not exist. Creating directory: $TargetProjectPath" -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path $TargetProjectPath | Out-Null
}

$TargetAgentsDir = Join-Path $TargetProjectPath ".agents"
$TargetDocsDir   = Join-Path $TargetProjectPath "docs/loops"
$TargetCodeDir   = Join-Path $TargetProjectPath "loop-library/code"
$TargetDevContainerDir = Join-Path $TargetProjectPath ".devcontainer"

# 2. Provision Directory Structure
$DirsToCreate = @($TargetAgentsDir, $TargetDocsDir, $TargetCodeDir, $TargetDevContainerDir)
foreach ($Dir in $DirsToCreate) {
    if (-not (Test-Path -Path $Dir)) {
        New-Item -ItemType Directory -Force -Path $Dir | Out-Null
    }
}

# 3. Copy Shared Standards and specifications
Write-Host "[+] Porting shared standards and principles..." -ForegroundColor Cyan
$SharedSrc = Join-Path $SrcLibRoot "shared"
$SharedDest = Join-Path $TargetDocsDir "shared"
if (Test-Path -Path $SharedSrc) {
    if (-not (Test-Path -Path $SharedDest)) {
        New-Item -ItemType Directory -Force -Path $SharedDest | Out-Null
    }
    Copy-Item -Path "$SharedSrc/*" -Destination $SharedDest -Recurse -Force
    Write-Host "    - Copy complete: docs/loops/shared/" -ForegroundColor Gray
} else {
    Write-Warning "Shared directory not found at: $SharedSrc"
}

# 4. Contextual Loop Selection and Copy
Write-Host "[+] Porting contextual loop workflows..." -ForegroundColor Cyan

$SelectedLoops = @()

switch ($ProjectType) {
    "Greenfield" {
        $SelectedLoops = @(
            "governance/LOOP-301-ADR-Generation.md",
            "engineering/LOOP-104-Documentation.md",
            "core/LOOP-001-Architecture-Discovery.md",
            "engineering/LOOP-103-Test-Generation.md",
            "core/LOOP-005-Implementation.md",
            "platform/LOOP-202-Integration-Validation.md",
            "governance/LOOP-304-Release-Readiness.md"
        )
    }
    "Brownfield" {
        $SelectedLoops = @(
            "core/LOOP-002-Context-Assembly.md",
            "engineering/LOOP-103-Test-Generation.md",
            "core/LOOP-005-Implementation.md",
            "core/LOOP-006-Verification.md",
            "engineering/LOOP-102-Refactoring.md",
            "governance/LOOP-303-Compliance.md"
        )
    }
    "Modernization" {
        $SelectedLoops = @(
            "core/LOOP-001-Architecture-Discovery.md",
            "engineering/LOOP-105-Code-Review.md",
            "engineering/LOOP-103-Test-Generation.md",
            "engineering/LOOP-102-Refactoring.md",
            "platform/LOOP-204-API-Contract-Validation.md",
            "governance/LOOP-302-Documentation-Governance.md"
        )
    }
    "IncidentResponse" {
        $SelectedLoops = @(
            "core/LOOP-002-Context-Assembly.md",
            "engineering/LOOP-101-Bug-Fixing.md",
            "engineering/LOOP-103-Test-Generation.md",
            "core/LOOP-005-Implementation.md",
            "core/LOOP-006-Verification.md",
            "core/LOOP-007-Reflection.md"
        )
    }
    "All" {
        # Copy everything recursively from the loops directory
        $LoopsSrc = Join-Path $SrcLibRoot "loops"
        if (Test-Path -Path $LoopsSrc) {
            Copy-Item -Path "$LoopsSrc/*" -Destination $TargetDocsDir -Recurse -Force
            Write-Host "    - Copied all loops recursively to docs/loops/" -ForegroundColor Gray
        }
    }
}

if ($ProjectType -ne "All") {
    foreach ($LoopPath in $SelectedLoops) {
        $FullSrcPath = Join-Path "$SrcLibRoot/loops" $LoopPath
        if (Test-Path -Path $FullSrcPath) {
            $Category = Split-Path $LoopPath -Parent
            $CategoryDestDir = Join-Path $TargetDocsDir $Category
            if (-not (Test-Path -Path $CategoryDestDir)) {
                New-Item -ItemType Directory -Force -Path $CategoryDestDir | Out-Null
            }
            Copy-Item -Path $FullSrcPath -Destination $CategoryDestDir -Force
            Write-Host "    - Imported loop: $LoopPath" -ForegroundColor Gray
        } else {
            Write-Warning "Loop file not found: $FullSrcPath"
        }
    }
}

# 5. Provision Agent Customization & Templates
Write-Host "[+] Porting templates and Agent rules..." -ForegroundColor Cyan
$TemplateSrc = Join-Path $SrcLibRoot "templates"
$TemplateDest = Join-Path $TargetAgentsDir "templates"
if (Test-Path -Path $TemplateSrc) {
    if (-not (Test-Path -Path $TemplateDest)) {
        New-Item -ItemType Directory -Force -Path $TemplateDest | Out-Null
    }
    Copy-Item -Path "$TemplateSrc/*" -Destination $TemplateDest -Recurse -Force
    
    # Copy AGENTS-TEMPLATE.md as base AGENTS.md in the customizations root
    $AgentsDestFile = Join-Path $TargetAgentsDir "AGENTS.md"
    if (-not (Test-Path -Path $AgentsDestFile)) {
        Copy-Item -Path (Join-Path $TemplateSrc "AGENTS-TEMPLATE.md") -Destination $AgentsDestFile -Force
        Write-Host "    - Created base .agents/AGENTS.md" -ForegroundColor Gray
    }
}

# 6. Copy Programmatic Rule Engine & Execution Core (Java code)
Write-Host "[+] Porting rule engine execution library..." -ForegroundColor Cyan
$CodeSrc = Join-Path $SrcLibRoot "code"
if (Test-Path -Path $CodeSrc) {
    Copy-Item -Path "$CodeSrc/*" -Destination $TargetCodeDir -Recurse -Force
    Write-Host "    - Copy complete: loop-library/code/" -ForegroundColor Gray

    # Grab Gradle wrapper from Conductor repository root (2 levels up from code directory)
    $WorkspaceRoot = (Get-Item $SrcLibRoot).Parent.FullName
    $GradleSrcDir = Join-Path $WorkspaceRoot "gradle"
    $GradleW = Join-Path $WorkspaceRoot "gradlew"
    $GradleWBat = Join-Path $WorkspaceRoot "gradlew.bat"

    if ((Test-Path $GradleSrcDir) -and (Test-Path $GradleW) -and (Test-Path $GradleWBat)) {
        Copy-Item -Path $GradleSrcDir -Destination $TargetCodeDir -Recurse -Force
        Copy-Item -Path $GradleW -Destination $TargetCodeDir -Force
        Copy-Item -Path $GradleWBat -Destination $TargetCodeDir -Force
        Write-Host "    - Added standalone Gradle wrapper files to loop-library/code/" -ForegroundColor Gray
    } else {
        Write-Warning "Gradle wrapper files not found in Conductor root directory. Stakeholders must supply Gradle."
    }
}

# 7. Configure Dev Container settings
Write-Host "[+] Setting up Dev Container environment..." -ForegroundColor Cyan

$DevContainerFile = Join-Path $TargetDevContainerDir "devcontainer.json"
$SetupScriptFile = Join-Path $TargetDevContainerDir "devcontainer-setup.sh"

$DevContainerExists = Test-Path -Path $DevContainerFile

if (-not $DevContainerExists -or $OverwriteDevContainer) {
    # Generate devcontainer.json
    $DevContainerContent = @'
{
  "name": "Loop Engineering Dev Environment",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {
      "moby": true,
      "version": "latest"
    },
    "ghcr.io/devcontainers/features/java:1": {
      "version": "21"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "redhat.vscode-yaml",
        "vscjava.vscode-java-pack"
      ]
    }
  },
  "postCreateCommand": "bash .devcontainer/devcontainer-setup.sh"
}
'@
    Set-Content -Path $DevContainerFile -Value $DevContainerContent -Encoding utf8
    Write-Host "    - Generated .devcontainer/devcontainer.json" -ForegroundColor Gray

    # Generate devcontainer-setup.sh
    $SetupScriptContent = @'
#!/usr/bin/env bash
set -euo pipefail

echo "=== Initializing Loop Engineering Dev Container ==="

# Compile rule engine core and run unit validations
if [ -d "loop-library/code" ]; then
    echo "Bootstrapping loop Java rule engine..."
    chmod +x loop-library/code/gradlew || true
    (cd loop-library/code && ./gradlew test) || echo "Warning: Initial unit tests failed or skipped."
fi

echo "=== Dev Container Loop Setup Completed Successfully ==="
'@
    Set-Content -Path $SetupScriptFile -Value $SetupScriptContent -Encoding utf8
    Write-Host "    - Generated .devcontainer/devcontainer-setup.sh" -ForegroundColor Gray
} else {
    Write-Host "    - Dev Container files already exist. Skipping. (Use -OverwriteDevContainer to force update)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== Configuration Ported Successfully! ===" -ForegroundColor Green
Write-Host "To execute loops:"
Write-Host "  1. Open target project in VS Code."
Write-Host "  2. Run 'Dev Containers: Reopen in Container' when prompted."
Write-Host "  3. The container will automatically compile rules and cache dependencies."
Write-Host "  4. Use the templates in .agents/templates/ to run loop cycles." -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
