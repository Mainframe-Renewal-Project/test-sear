
from helper import successful_return_codes

# Import SEAR
from sear import sear


def test_setropts_extract():
    extract_result = sear(
        {
        "operation": "extract",
        "admin_type": "racf-options",
        },
    )
    assert extract_result.result["return_codes"] == successful_return_codes
