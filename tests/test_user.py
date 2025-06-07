# Import SEAR
from helper import successful_return_codes
from sear import sear


def test_add_user(delete_user):
    add_result = sear(
            {
            "operation": "add", 
            "admin_type": "user", 
            "userid": delete_user,
            "traits": {
                "base:installation_data": "USER GENERATED DURING SEAR TESTING, NOT IMPORTANT",
            },
            },
        )
    assert add_result.result["return_codes"] == successful_return_codes

def test_extract_user(create_user):
    extract_result = sear(
            {
            "operation": "extract",
            "admin_type": "user",
            "userid": create_user
            },
        )
    assert extract_result.result["return_codes"] == successful_return_codes

def test_alter_user(create_user):
    alter_result = sear(
            {
            "operation": "alter", 
            "admin_type": "user", 
            "userid": create_user,
            "traits": {
                "omvs:default_shell": "/bin/zsh",
            },
            },
        )
    assert alter_result.result["return_codes"] == successful_return_codes

def test_delete_user(create_user):
    delete_result = sear(
            {
            "operation": "delete",
            "admin_type": "user",
            "userid": create_user,
            },
        )
    assert delete_result.result["return_codes"] == successful_return_codes
