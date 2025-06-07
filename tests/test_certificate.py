
from helper import keyring_not_found_return_codes, successful_return_codes

# Import SEAR
from sear import sear


def test_extract_certificate_not_found():
    add_result = sear(
        {
        "operation": "extract", 
        "admin_type": "keyring", 
        "keyring": "SEARNOTFOUND",
        "owner": "IBMUSER",
        },
    )
    assert "errors" not in str(add_result.result)
    assert add_result.result["return_codes"] == keyring_not_found_return_codes
