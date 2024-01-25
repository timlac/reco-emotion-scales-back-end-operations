import json

import requests
from auth import get_id_token


id_token = get_id_token()

# Replace with your API endpoint URL
api_url = 'https://xxpy3ht9ke.execute-api.eu-west-1.amazonaws.com/prod/users'

# Set the authorization header with the ID Token obtained from Cognito
headers = {
    'Authorization': 'Bearer ' + id_token
}

# Make a GET request (you can use other HTTP methods like POST, PUT, etc.)
response = requests.get(api_url, headers=headers)

api_data = []

# Check the response status code and handle the API response as needed
if response.status_code == 200:
    api_data = response.json()
    # Process the API data here
    print(api_data)
else:
    print('API request failed with status code:', response.status_code)

with open('users.json', 'w') as f:
    json.dump(api_data, f)
