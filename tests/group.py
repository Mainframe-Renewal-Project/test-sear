# Import SEAR
from sear import sear

add_result = sear(
        {
        "operation": "add", 
        "admin_type": "group", 
        "userid": "SEARG1",
        "traits": {
            "base:installation_data": "GROUP GENERATED DURING SEAR TESTING, NOT IMPORTANT",
        },
        },
    )

print(add_result.result)

extract_result = sear(
        {
        "operation": "extract",
        "admin_type": "group",
        "userid": "SEARG1"
        },
    )

print(extract_result.result)

alter_result = sear(
        {
        "operation": "alter", 
        "admin_type": "group", 
        "userid": "SEARG1",
        "traits": {
            "omvs:auto_gid": True,
        },
        },
    )

print(alter_result.result)

delete_result = sear(
        {
        "operation": "delete",
        "admin_type": "group",
        "userid": "SEARG1",
        },
    )

print(delete_result.result)