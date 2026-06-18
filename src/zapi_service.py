import requests

from config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN
)


def send_message(phone, name):

    url = (
        f"https://api.z-api.io/"
        f"instances/{ZAPI_INSTANCE_ID}"
        f"/token/{ZAPI_TOKEN}/send-text"
    )

    payload = {
        "phone": phone,
        "message": f"Olá, {name} tudo bem com você?"
    }

    response = requests.post(
        url,
        json=payload
    )

    return response