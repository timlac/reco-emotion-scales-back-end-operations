import boto3
import json
import os

session = boto3.Session(profile_name='rackspaceAcc')


# Initialize DynamoDB client
dynamodb = session.resource('dynamodb')

# Retrieve the DynamoDB table name from the environment variables
table_name = 'MainStack-VideoMetadataTable0E75C188-P8TSTL0OU3JF'
table = dynamodb.Table(table_name)

# Scan table to retrieve all users
response = table.scan()
items = response.get('Items', [])
