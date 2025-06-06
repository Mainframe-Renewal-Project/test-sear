# This shell script runs the tests against a real build of SEAR
# It also cleans up after them in case they failed

set -e

DIRECTORY="venv"

function run_test {
    python -m venv venv
    
    # Activate virtual environment
    . venv/bin/activate

    pip install ./artifacts/*.whl

    # Runs the various test scripts
    pytest ./tests/user.py
    
}

# Run test
run_test
