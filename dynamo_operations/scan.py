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
table_name = 'MainStack-VideoMetadataTable0E75C188-P8TSTL0OU3JF'
table = dynamodb.Table(table_name)

# Scan table to retrieve all users
response = table.scan()
items = response.get('Items', [])

df = pd.DataFrame.from_records(items)

df.to_csv("../files/items.csv")

emotion_id_counts = df["emotion_id"].value_counts()

# Map emotion IDs to actual emotions using your Mapper class
mapped_emotions = emotion_id_counts.index.map(Mapper.get_emotion_from_id)

# Create a histogram plot
plt.figure(figsize=(12, 6))
plt.bar(mapped_emotions, emotion_id_counts.values)

# Customize the plot
plt.xlabel('Emotion')
plt.ylabel('Frequency')
plt.title('Frequency of Emotions')
plt.xticks(rotation=90)  # Rotate x-axis labels for readability

plt.tight_layout()

# Show the plot
plt.show()
