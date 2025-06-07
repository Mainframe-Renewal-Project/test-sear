
from helper import keyring_not_found_return_codes, successful_return_codes

# Import SEAR
from sear import sear


def test_extract_keyring_not_found():
    not_found_result = sear(
        {
        "operation": "extract", 
        "admin_type": "keyring", 
        "keyring": "SEARNOTFOUND",
        "owner": "IBMUSER",
        },
    )
    assert not_found_result.result["return_codes"] == keyring_not_found_return_codes

def test_extract_keyring(create_keyring):
    keyring, owner = create_keyring
    extract_result = sear(
        {
        "operation": "extract", 
        "admin_type": "keyring", 
        "keyring": keyring,
        "owner": owner,
        },
    )
    assert extract_result.result["return_codes"] == successful_return_codes
