# This shell script runs the tests against a real build of SEAR
# It also cleans up after them in case they failed

set -e

repo_dir="$PWD/sear"
repo_ref="main"
artifacts_dir="$PWD/artifacts"
report_file="$PWD/report.md"

function run_test {
    pushd "$repo_dir"

    python -m venv venv

    # Fetch tests
    echo "Fetching ref: $repo_ref"

    git fetch --tags origin "$repo_ref"
    git clean -dxf
    git checkout "origin/$repo_ref"
    
    # Activate virtual environment
    . venv/bin/activate

    pip install $artifacts_dir/*.whl
    rm $artifacts_dir/*

    pip install pytest pytest-md

    # Runs the various test scripts
    pytest -vv --md=$report_file

    popd
}

# Run test
run_test
