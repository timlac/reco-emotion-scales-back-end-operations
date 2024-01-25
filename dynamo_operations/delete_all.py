import boto3
session = boto3.Session(profile_name='rackspaceAcc')


# Initialize DynamoDB client
dynamodb = session.resource('dynamodb')

# Retrieve the DynamoDB table name from the environment variables
table_name = 'EmotionCategoriesStack-EmotionCategoriesResponseTable0D9603EB-S8FK1CPQXNDS'
table = dynamodb.Table(table_name)

scan = table.scan(
    ProjectionExpression='#k',
    ExpressionAttributeNames={
        '#k': 'id'
    }
)

with table.batch_writer() as batch:
    for each in scan['Items']:
        batch.delete_item(Key=each)