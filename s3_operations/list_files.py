import boto3
import os
import time
from pathlib import Path
from dynamo_operations.insert_metadata import insert_meta

from nexa_coding_interpreter.metadata import Metadata

from config import sex_dict, prosody_dict

t1 = time.time()


session = boto3.Session(profile_name='rackspaceAcc')

s3_client = session.client('s3')

bucket_name = 'mainstack-videofiles720pc366226e-haxvasmgqgdh'


def list_objects(bucket, continuation_token=None):
    if continuation_token:
        resp = s3_client.list_objects_v2(Bucket=bucket, ContinuationToken=continuation_token)
    else:
        resp = s3_client.list_objects_v2(Bucket=bucket)
    return resp


keys = []
token = None
while True:
    response = list_objects(bucket_name, token)
    keys.extend([obj['Key'] for obj in response.get('Contents', [])])

    # Check if more objects are available
    if response.get('IsTruncated'):
        token = response.get('NextContinuationToken')
    else:
        break

t2 = time.time()

print(len(keys))


print(f'Elapsed time: {t2-t1}')


for key in keys:
    filename = Path(key).stem

    metadata = Metadata(filename)

    sex = sex_dict[metadata.video_id]
    prosody = prosody_dict[metadata.video_id]

    insert_meta(key, metadata, sex, prosody)






