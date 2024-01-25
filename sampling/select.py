import pandas as pd
import boto3
import json
import os
import matplotlib.pyplot as plt
from boto3.dynamodb.conditions import Attr
from dynamo_operations.serializer import to_serializable


session = boto3.Session(profile_name='rackspaceAcc')
# Initialize DynamoDB client
dynamodb = session.resource('dynamodb')
# Retrieve the DynamoDB table name from the environment variables
table_name = 'EmotionCategoriesStack-EmotionCategoriesResponseTable0D9603EB-S8FK1CPQXNDS'
table = dynamodb.Table(table_name)

print(table)

user_id = "a"


# Step 2: Retrieve existing user's data
response = table.get_item(
    Key={'id': user_id}
)

if 'Item' in response:

    print(response)