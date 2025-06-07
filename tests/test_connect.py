
from helper import successful_return_codes

# Import SEAR
from sear import sear


def test_add_connect(create_user):
    add_result = sear(
            {
            "operation": "alter", 
            "admin_type": "group-connection", 
            "userid": create_user,
            "group": "SEARDUMY",
            "traits": {
                "base:owner": "SYS1",
            },
            },
        )
    assert "errors" not in str(add_result.result)
    assert add_result.result["return_codes"] == successful_return_codes