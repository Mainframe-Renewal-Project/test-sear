# Import SEAR
from sear import sear

from helper import successful_return_codes

def test_setropts_extract(delete_user):
    extract_result = sear(
        {
        "operation": "extract",
        "admin_type": "racf-options",
        },
    )
    assert extract_result.result["return_codes"] == successful_return_codes
