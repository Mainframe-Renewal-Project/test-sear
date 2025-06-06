# Import SEAR
from sear import sear

add_result = sear(
        {
        "operation": "add", 
        "admin_type": "resource", 
        "resource": "sear.test",
        "class": "facility",
        "traits": {
            "base:installation_data": "RESOURCE PROFILE GENERATED DURING SEAR TESTING, NOT IMPORTANT",
        },
        },
    )

print(add_result.result)

refresh_result = sear(
    {
        "operation": "alter", 
        "admin_type": "racf-options", 
        "traits": {
            "base:refresh": True,
        },
    },
)

print(f"refresh result: {refresh_result.result}")

extract_result = sear(
        {
        "operation": "extract",
        "admin_type": "resource",
        "resource": "SEAR.TEST",
        "class": "FACILITY",
        },
    )

print(extract_result.result)

alter_result = sear(
        {
        "operation": "alter", 
        "admin_type": "resource", 
        "resource": "sear.test",
        "class": "facility",
        "traits": {
            "base:universal_access": "READ",
        },
        },
    )

print(alter_result.result)

delete_result = sear(
        {
        "operation": "delete",
        "admin_type": "resource",
        "resource": "sear.test",
        "class": "facility",
        },
    )

print(delete_result.result)