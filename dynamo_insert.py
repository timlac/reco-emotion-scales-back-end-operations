import boto3

session = boto3.Session(profile_name='rackspaceAcc')

# Now you can use this session to create clients and resources for your AWS services
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('MainStack-UsersEmotionScales6BA5F65B-CX50A07KW19R')


