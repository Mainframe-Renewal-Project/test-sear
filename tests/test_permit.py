
from helper import successful_return_codes

# Import SEAR
from sear import sear


def test_add_dataset_permit(create_user, create_dataset):
    """This test is supposed to succeed"""
    add_result = sear(
            {
            "operation": "alter", 
            "admin_type": "permission", 
            "data_set": create_dataset,
            "userid": create_user,
            "generic": True,
            "traits": {
                "base:access": "READ",
            },
            },
        )
    assert "errors" not in str(add_result.result)
    assert add_result.result["return_codes"] == successful_return_codes