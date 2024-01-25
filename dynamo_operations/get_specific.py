import boto3


session = boto3.Session(profile_name='rackspaceAcc')


# Initialize DynamoDB client
dynamodb = session.resource('dynamodb')

# Retrieve the DynamoDB table name from the environment variables
table_name = 'EmotionDataStack-surveytable310F762D-14SKRAJHU05VT'

table = dynamodb.Table(table_name)

response = table.get_item(
    Key={
        "survey_type": "categories",
        'survey_id': "142e4420ba988039b0036624e1152b1e23c0a7e78d3ac2057c392400c7c2c160"
    }
)
item = response.get('Item')  # Get the single item

print(item)
