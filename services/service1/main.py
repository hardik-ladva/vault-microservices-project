import requests

VAULT_ADDR = "http://127.0.0.1:8200"
ROLE_ID = "cb749a62-76f9-a751-a8b0-2f9041228d9f"
SECRET_ID = "ebe3d00c-d3ee-16fb-25b1-2541e764dcf7"

# AppRole Login
login = requests.post(f"{VAULT_ADDR}/v1/auth/approle/login", json={
    "role_id": ROLE_ID,
    "secret_id": SECRET_ID
})
token = login.json()["auth"]["client_token"]

# Access Secret
secret = requests.get(
    f"{VAULT_ADDR}/v1/secret/data/service1",
    headers={"X-Vault-Token": token}
)
print(secret.json())
