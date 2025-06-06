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
    python ./tests/user.py
    python ./tests/group.py
    python ./tests/dataset.py
    python ./tests/resource.py
}

function clean_up {
    # Delete test user, in case test fails
    /bin/tsocmd "DELUSER SEART1"

    # Delete group, in case test fails
    /bin/tsocmd "DELGROUP SEARG1"

    # Delete dataset profile, in case test fails
    /bin/tsocmd "DELDSD DA(SEARTEST.**.**) GENERIC"

    # Delete resource profile, in case test fails
    /bin/tsocmd "RDELETE APPL (SEAR.TEST)"
}

# Run test
run_test

# Run emergency clean up function
# This ensures no gunk is left on the system
clean_up