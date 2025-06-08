
from helper import successful_return_codes

# Import SEAR
from sear import sear


def test_connect(create_user):
    connect_result = sear(
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
    assert "errors" not in str(connect_result.result)
    assert connect_result.result["return_codes"] == successful_return_codes