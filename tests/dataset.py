# Import SEAR
from sear import sear

add_result = sear(
        {
        "operation": "add", 
        "admin_type": "data-set", 
        "data_set": "SEARTEST.**",
        "traits": {
            "base:installation_data": "DATASET PROFILE GENERATED DURING SEAR TESTING, NOT IMPORTANT",
        },
        },
    )

print(add_result.result)

extract_result = sear(
        {
        "operation": "extract",
        "admin_type": "data-set", 
        "data_set": "SEARTEST.**",
        },
    )

print(extract_result.result)

delete_result = sear(
        {
        "operation": "delete",
        "admin_type": "data-set", 
        "data_set": "SEARTEST.**",
        },
    )

print(delete_result.result)