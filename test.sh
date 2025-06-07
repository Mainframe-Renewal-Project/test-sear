# This shell script runs the tests against a real build of SEAR
# It also cleans up after them in case they failed

set -e

DIRECTORY="venv"

function run_test {
    python -m venv venv
    
    # Activate virtual environment
    . venv/bin/activate

    pip install ./artifacts/*.whl
    rm ./artifacts/*

    pip install pytest pytest-md

    # Runs the various test scripts
    pytest ./tests/ -vv --md=report.md
    
}

# Run test
run_test
