# This shell script runs the tests and cleans up after them in case they failed

set -e

DIRECTORY="./venv"

function run_test {
    if [ -d "$DIRECTORY" ]; then
        python -m venv venv
    fi
    
    . .venv/bin/activate

    pip install ./artifacts/*.whl

    python3 ./tests/user.py
    python3 ./tests/group.py
    python3 ./tests/dataset.py
    python3 ./tests/resource.py
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