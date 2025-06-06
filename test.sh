# This shell script runs the tests and cleans up after them in case they failed

set -e

function run_test {

}

function clean_up {
    # Delete test user, in case test fails
    /bin/tsocmd "DELUSER SEART1"

    # Delete group, in case test fails
    /bin/tsocmd "DELGROUP SEARG1"

    # Delete resource profile, in case test fails
    /bin/tsocmd "RDELETE APPL (SEAR.TEST)"

    # Delete dataset profile, in case test fails
    /bin/tsocmd "DELDSD DA(SEARTEST.**.**) GENERIC"
}

# Run test
run_test

# Run clean up function
clean_up