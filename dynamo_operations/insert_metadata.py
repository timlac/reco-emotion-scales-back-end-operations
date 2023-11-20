import boto3

table_name = 'MainStack-VideoMetadataTable0E75C188-P8TSTL0OU3JF'

session = boto3.Session(profile_name='rackspaceAcc')

# Initialize DynamoDB client
dynamodb = session.client('dynamodb')


def insert_meta(key, metadata, sex, prosody):

    if metadata.intensity_level:
        intensity_level = str(metadata.intensity_level)
    else:
        intensity_level = "0"

    response = dynamodb.put_item(
        TableName=table_name,
        Item={
            "filename": {"S": key},
            "video_id": {"S": metadata.video_id},
            "emotion_id": {"N": str(metadata.emotion_1_id)},
            "intensity_level": {"N": intensity_level},
            "sex": {"S": sex},
            "prosody": {"S": prosody}
        }
    )
    print(response)
