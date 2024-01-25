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


user_id = "a"
filename = 'A437_hap_p_3.mp4'
reply = "6"

# Step 2: Retrieve existing user's data
response = table.get_item(
    Key={'id': user_id}
)

if 'Item' in response:

    print(response)

    dynamo_item = response['Item']

    print(dynamo_item)

    update_idx = None

    for idx, user_item in enumerate(dynamo_item['user_items']):
        if user_item['filename'] == filename:
            if user_item['reply'] != "":
                print("error, reply already exists...")
            else:
                user_item['reply'] = reply
            update_idx = idx

    if update_idx is None:
        print("error, filename doesn't exist in file")

    print(update_idx)

    # Update the item if found
    if update_idx is not None:
        update_response = table.update_item(
            Key={'id': user_id},
            UpdateExpression=f'SET user_items[{update_idx}].reply = :val, '
                             f'user_items[{update_idx}].has_reply = :hasReplyVal',
            ExpressionAttributeValues={
                ':val': {'S': reply},
                ':hasReplyVal': {'N': '1'}  # 'N' for Number type
            }
        )
        print(update_response)
else:
    print("error")


#
#
# print(response)
#
# dynamo_item = response['Item']
#
# for item in dynamo_item['items']:
#     if item['filename'] == filename:
#         if item['reply'] != "":
#             print("error, reply already exists...")
#         else:
#             item['reply'] = reply
#
# print(dynamo_item["items"])
#
# ret = json.dumps(dynamo_item, default=to_serializable)
# print(ret)
