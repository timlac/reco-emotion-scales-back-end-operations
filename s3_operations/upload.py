import boto3
from glob import glob
import logging
from pathlib import Path
from nexa_coding_interpreter.metadata import Metadata

import os
from botocore.exceptions import ClientError

files_path = "/home/tim/Work/nexa/nexa-audio-normalization/data/peak_normalized_box_downloads"
log_file_path = "../files/logs/s3_upload.log"

logging.basicConfig(filename=log_file_path, level=logging.INFO, filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')


class S3Uploader:
    """
    A class that uploads files to AWS S3
    """

    def __init__(self):
        # Configure the session with your profile
        session = boto3.Session(profile_name='rackspaceAcc')

        self.s3 = session.client('s3')

        self.bucket_name = 'reco-video-files'

    def upload(self, path, file_name):
        """
        Uploads a file to S3
        :param path: the local path
        :param file_name: the file name
        :return:
        """

        print(f'{path=}')
        print(f'{file_name=}')

        object_key = f'fmri/{file_name}'

        self.s3.upload_file(path, self.bucket_name, object_key)

    def file_name_exists(self, file_name):
        """
        :param file_name: check if this filename already exists in bucket
        :return: True if exists, False otherwise
        """
        try:
            # Try to retrieve the metadata for the object with the given key
            self.s3.head_object(Bucket=self.bucket_name, Key=file_name)
        except ClientError as e:
            # If a ClientError is raised, it means that the object does not exist
            # You can go ahead and upload the file
            if e.response['Error']['Code'] == '404':
                return False
            else:
                # If the error code is not 404, it means that there was some other error
                print(f'Error: {e}')
        else:
            # If no exception is raised, it means that the object with the given key exists
            return True


def process_files(directory):
    """
    :param directory: dir to process recursively
    """

    uploader = S3Uploader()

    paths = glob(directory + "**/*.mp4")

    for filepath in paths:
        filename = Path(filepath).stem
        metadata = Metadata(filename)

        if (not metadata.mix
                and (metadata.intensity_level in [2, 3] or metadata.emotion_1_abr == "neu")
                # Two error files were added manually, see README
                and not metadata.error):
            file_name = os.path.basename(filepath)

            if uploader.file_name_exists(file_name):
                logging.info("file name {} already exists, skipping: ".format(file_name))
            else:
                logging.info("uploading file: " + str(file_name))
                # Upload the file to S3
                uploader.upload(filepath, file_name)


process_files(files_path)
