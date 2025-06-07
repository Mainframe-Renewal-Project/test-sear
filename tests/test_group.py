
from helper import group_not_found_return_codes, successful_return_codes

# Import SEAR
from sear import sear


def test_add_group(delete_group):
    add_result = sear(
            {
            "operation": "add", 
            "admin_type": "group", 
            "group": delete_group,
            "traits": {
                "base:installation_data": "GROUP GENERATED DURING SEAR TESTING, NOT IMPORTANT",
            },
            },
        )
    assert add_result.result["return_codes"] == successful_return_codes

def test_extract_group(create_group):
    extract_result = sear(
            {
            "operation": "extract",
            "admin_type": "group",
            "group": create_group,
            },
        )
    assert extract_result.result["return_codes"] == successful_return_codes

def test_group_not_found():
    not_found_result = sear(
            {
            "operation": "extract",
            "admin_type": "group", 
            "data_set": "BADGRP",
            },
        )
    assert "errors" in str(not_found_result.result)
    assert not_found_result.result["return_codes"] == group_not_found_return_codes

def test_alter_group(create_group):
    alter_result = sear(
            {
            "operation": "alter", 
            "admin_type": "group", 
            "group": create_group,
            "traits": {
                "omvs:auto_gid": True,
            },
            },
        )
    assert alter_result.result["return_codes"] == successful_return_codes

def test_delete_group(create_group):
    delete_result = sear(
            {
            "operation": "delete",
            "admin_type": "group",
            "group": create_group,
            },
        )
    assert delete_result.result["return_codes"] == successful_return_codes
