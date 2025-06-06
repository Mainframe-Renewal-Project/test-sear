# This shell script runs the tests and cleans up after them in case they failed

set -e

function run_test {

}

function clean_up {
    /bin/tsocmd "deluser SEART1"
}

# Run test
run_test

# Run clean up function
clean_up