# import boto3
import base64
import requests

# Storing secrets directly within code is not a best practice
# Using a tool like AWS SSM or Secrets Manager may be a better option for you
# ssm = boto3.client('ssm')

# MARKETPLACE_API_KEY = ssm.get_parameter(
#     Name='MARKETPLACE_API_KEY',
#     WithDecryption=True
# )['Parameter']['Value']

# MARKETPLACE_API_SECRET = ssm.get_parameter(
#     Name='MARKETPLACE_API_SECRET',
#     WithDecryption=True
# )['Parameter']['Value']

MARKETPLACE_API_KEY = 'YOUR_API_KEY'
MARKETPLACE_API_SECRET = 'YOUR_API_SECRET'


def get_marketplace_token() -> str:
    CREDENTIAL_BYTES = str(MARKETPLACE_API_KEY + ':' + MARKETPLACE_API_SECRET).encode('ascii')
    CREDENTIAL_B64 = base64.b64encode(CREDENTIAL_BYTES).decode()
    headers = {
        'Authorization': f'Basic {CREDENTIAL_B64}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials',
        'scope': 'https://myresourceserver1.com/marketplace'
    }
    response = requests.post('https://oauth.totogi.io/oauth2/token', headers=headers, data=data)
    token = response.json()['access_token']
    return token
