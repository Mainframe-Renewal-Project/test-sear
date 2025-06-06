# Import SEAR
from sear import sear

add_result = sear(
        {
        "operation": "add", 
        "admin_type": "user", 
        "userid": "SEART1",
        "traits": {
            "base:installation_data": "USER GENERATED DURING SEAR TESTING, NOT IMPORTANT",
        },
        },
    )

print(add_result.result)

extract_result = sear(
        {
        "operation": "extract",
        "admin_type": "user",
        "userid": "SEART1"
        },
    )

print(extract_result.result)

alter_result = sear(
        {
        "operation": "alter", 
        "admin_type": "user", 
        "userid": "SEART1",
        "traits": {
            "omvs:default_shell": "/bin/zsh",
        },
        },
    )

print(alter_result.result)

delete_result = sear(
        {
        "operation": "delete",
        "admin_type": "user",
        "userid": "SEART1",
        },
    )

print(delete_result.result)