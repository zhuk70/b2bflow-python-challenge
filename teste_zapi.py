import requests

INSTANCE_ID = "3F4D63819F8EB17685CECA63B40AA2AA"
TOKEN = "721307175AB449FC595B0231"

url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

payload = {
    "phone": "5511947936426",
    "message": "Teste da Z-API"
}

response = requests.post(
    url,
    json=payload
)
print("Status:", response.status_code)
print("Resposta completa:")
print(response.text)