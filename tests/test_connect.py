
from helper import successful_return_codes

# Import SEAR
from sear import sear

from tests.conftest import run_tso_command


def test_add_connect(create_user):
    add_result = sear(
            {
            "operation": "add", 
            "admin_type": "group-connection", 
            "userid": create_user,
            "group": "SEARDUMY",
            "traits": {
                "base:owner": "SYS1",
            },
            },
        )
    run_tso_command(f"REMOVE {create_user} GROUP(SEARDUMY)")
    assert add_result.result["return_codes"] == successful_return_codes