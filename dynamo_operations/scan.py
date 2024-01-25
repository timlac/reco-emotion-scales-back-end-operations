import time

import boto3
import json
import os
import pandas as pd
import matplotlib.pyplot as plt


from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper


session = boto3.Session(profile_name='rackspaceAcc')


# Initialize DynamoDB client
dynamodb = session.resource('dynamodb')

# Retrieve the DynamoDB table name from the environment variables
table_name = 'EmotionCategoriesStack-EmotionCategoriesResponseTable0D9603EB-S8FK1CPQXNDS'
table = dynamodb.Table(table_name)


def scan_full_table(db_table, limit=None):
    ret = []
    resp = db_table.scan()
    ret += resp['Items']

    while 'LastEvaluatedKey' in resp:
        resp = db_table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'])
        ret += resp['Items']

    return ret


start = time.time()

items = scan_full_table(table)

end = time.time()

print(end - start)
# Scan table to retrieve all users
# response = table.scan()
# items = response.get('Items', [])

start = time.time()

for idx, survey in enumerate(items):
    count = sum(1 for item in survey["survey_items"] if item["has_reply"] == 1)
    total = len(survey["survey_items"])

    items[idx]["progress"] = count / total

end = time.time()

print(end - start)

start = time.time()


for idx, survey in enumerate(items):
    count = sum(1 for item in survey["survey_items"] if item["emotion_id"] == item["reply"])
    total = len(survey["survey_items"])

    items[idx]["accuracy"] = count / total

end = time.time()

print(end - start)
# df.to_csv("../files/items.csv")
#
# emotion_id_counts = df["emotion_id"].value_counts()
#
# # Map emotion IDs to actual emotions using your Mapper class
# mapped_emotions = emotion_id_counts.index.map(Mapper.get_emotion_from_id)
#
# # Create a histogram plot
# plt.figure(figsize=(12, 6))
# plt.bar(mapped_emotions, emotion_id_counts.values)
#
# # Customize the plot
# plt.xlabel('Emotion')
# plt.ylabel('Frequency')
# plt.title('Frequency of Emotions')
# plt.xticks(rotation=90)  # Rotate x-axis labels for readability
#
# plt.tight_layout()
#
# # Show the plot
# plt.show()
#
#
# df_sex_lust = df[df["emotion_id"] == 24]
# sex_sex_counts = df_sex_lust["sex"].value_counts()
# print(f'{sex_sex_counts=}')
#
# sex_counts = df["sex"].value_counts()
# print(f'{sex_counts=}')
