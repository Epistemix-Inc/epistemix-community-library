#!/bin/bash

# Notebook testing wrapper script
# Sets up a clean environment and runs notebook tests

set -euox pipefail

# Change to script's directory
cd "$(dirname "$0")"

echo "Setting up notebook testing environment..."

# Clean up any existing venv
if [ -d "test_venv" ]; then
    rm -rf test_venv
fi

# Create and activate fresh virtual environment
python -m venv test_venv
source test_venv/bin/activate

pip install --upgrade pip
pip install -r requirements_dev.txt

# Verify epx installation
echo "Verifying epx installation..."
python -c "from epx import FREDJob, FREDModelConfig, SynthPop; print('epx import successful')"

# Run the tests
echo "Running notebook tests..."
python -m pytest --nbmake . -v

TEST_RESULT=$?

deactivate
rm -rf test_venv

# Report results
if [ $TEST_RESULT -eq 0 ]; then
    echo "All notebook tests passed!"
else
    echo "Notebook tests failed with exit code $TEST_RESULT"
fi

exit $TEST_RESULT
