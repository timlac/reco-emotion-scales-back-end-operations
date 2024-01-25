import requests

# Define the API endpoint URL
api_url = 'https://xxpy3ht9ke.execute-api.eu-west-1.amazonaws.com/prod/users/aaa'

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response (if the API returns JSON)
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')
