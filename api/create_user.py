import json
import requests
from auth import get_id_token


with open("/home/tim/Work/recordix/reco-response-analysis/surveys.json") as f:
    data = json.load(f)


id_token = get_id_token()

api_url = 'https://xxpy3ht9ke.execute-api.eu-west-1.amazonaws.com/prod/users'

# Set the authorization header with the ID Token obtained from Cognito
headers = {
    'Authorization': 'Bearer ' + id_token
}


for idx, d in enumerate(data):
    print(idx)
    response = requests.post(api_url, headers=headers, json=d)
    print(response.json())
