
import subprocess
import pytest
import secrets

def run_tso_command(command: str):
    subprocess.run(f'tsocmd "{command}"', text=False, shell=True, check=True, capture_output=True)

@pytest.fixture
def delete_user():
    userid=f"SEAR{secrets.token_hex(2)}"
    yield userid
    try:
        run_tso_command(f"deluser {userid}")
    except:  # noqa: E722
        pass

@pytest.fixture
def create_user(delete_user):
    run_tso_command(f"adduser {delete_user} DATA('USER GENERATED DURING SEAR TESTING, NOT IMPORTANT')")
    yield delete_user

@pytest.fixture
def delete_group():
    groupid=f"SEAR{secrets.token_hex(2)}"
    yield groupid
    try:
        run_tso_command(f"delgroup {groupid}")
    except:  # noqa: E722
        pass

@pytest.fixture
def create_group(delete_group):
    run_tso_command(f"addgroup {delete_group} DATA('GROUP GENERATED DURING SEAR TESTING, NOT IMPORTANT')")
    yield delete_group