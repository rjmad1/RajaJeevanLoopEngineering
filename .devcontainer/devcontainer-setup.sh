#!/usr/bin/env bash
set -euo pipefail

echo "=== Initializing Loop Engineering Dev Container ==="

# Compile rule engine core and run unit validations
if [ -d "code" ]; then
    echo "Bootstrapping loop Java rule engine..."
    chmod +x code/gradlew || true
    (cd code && ./gradlew test) || echo "Warning: Initial unit tests failed or skipped."
fi

echo "=== Dev Container Loop Setup Completed Successfully ==="
