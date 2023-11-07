import os
import boto3

# Configure the session with your profile
session = boto3.Session(profile_name='personalAcc')
s3 = session.client('s3')

bucket_name = 'validation-experiment-video-files-01'
local_folder = '/home/tim/Work/recordix/reco-emotion-scales-back-end-operations/files/videos'

# Initialize the pagination token
continuation_token = None

while True:
    # List objects within the bucket with pagination
    if continuation_token:
        objects = s3.list_objects_v2(Bucket=bucket_name, ContinuationToken=continuation_token)
    else:
        objects = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in objects:
        for obj in objects['Contents']:
            # Define the local path where to save the object
            local_file_path = os.path.join(local_folder, obj['Key'])

            # Check if the file already exists
            if not os.path.exists(local_file_path):
                # Ensure the folder structure is in place
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

                # Download the file
                print(f"Downloading {obj['Key']}...")
                s3.download_file(bucket_name, obj['Key'], local_file_path)
            else:
                print(f"File {obj['Key']} already exists, skipping download.")
    else:
        print("No more files to download.")
        break

    # Check if the response is truncated (i.e., if there are more objects to retrieve)
    if objects['IsTruncated']:
        # If so, set the continuation token for the next batch
        continuation_token = objects['NextContinuationToken']
    else:
        # No more objects to retrieve, break the loop
        print("Download complete.")
        break

