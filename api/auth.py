import boto3
from dotenv import load_dotenv
import os
import requests


def get_id_token():
    load_dotenv()
    os.getenv("USERNAME")
    os.getenv("PASSWORD")

    # Initialize the AWS Cognito Identity Provider client
    client = boto3.client('cognito-idp', region_name='eu-west-1')

    # Define your Cognito User Pool details
    user_pool_id = 'eu-west-1_Iug3XSwRq'
    client_id = '2rer1p6jedoh35vtghn8s41s5p'
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    # Authenticate the user
    response = client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password,
        },
        ClientId=client_id,
    )

    # Check if the authentication was successful
    if 'AuthenticationResult' in response:
        # The user is authenticated, and you can access the ID Token and Access Token
        id_token = response['AuthenticationResult']['IdToken']
        access_token = response['AuthenticationResult']['AccessToken']
        print(f'ID Token: {id_token}')
        print(f'Access Token: {access_token}')

        return id_token
    else:
        # Authentication failed
        print('Authentication failed')
        raise Exception('Authentication')
