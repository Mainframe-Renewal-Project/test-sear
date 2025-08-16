# This shell script runs the tests against a real build of SEAR
# It also cleans up after them in case they failed

set -e

repo_dir="$PWD/sear"
repo_ref="dev"
artifacts_dir="$PWD/artifacts"
report_file="$PWD/report.md"

function run_test {
    pushd "$repo_dir"
    echo "Testing with Python: $2"

    # Fetch tests
    echo "Fetching ref: $repo_ref"

    git fetch --tags origin "$repo_ref"
    git clean -dxf
    git checkout "origin/$repo_ref"
   
    # Create virtual environment
    $1 -m venv ".venv-$1" --system-site-packages

    # Activate virtual environment
    "./.venv-$1/bin/activate"

    "./.venv-$1/bin/pip" install $artifacts_dir/*"$2"*.whl

    "./.venv-$1/bin/pip" install pytest pytest-md

    # Runs the various test scripts
    pytest python_tests -vv --md=$report_file

    popd
}

# Run test
run_test python3.12 cp312
run_test python3.13 cp313

rm $artifacts_dir/*