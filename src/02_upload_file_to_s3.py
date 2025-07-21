import os.path

import boto3
import time
from botocore.exceptions import ClientError
from config.config import *


class S3Uploader:
    def __init__(self, bucket_name=S3_BUCKET, prefix=S3_PREFIX, region=AWS_REGION):
        """
        Intitialise s3 uploader with configuration
        :param bucket_name: Name of the S3 bucket
        :param prefix: Prefix to add to object keys
        :param region: AWS region
        """
        self.bucket_name = bucket_name
        self.prefix = prefix
        self.region = region
        self.s3_client = self.create_s3_client()

    def create_s3_client(self) -> boto3.client:
        """
        create and configure s3 client
        :return: boto3.client : configured s3 client
        """
        try:
            return boto3.client(
                "s3",
                region_name=self.region,
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
        except Exception as e:
            print(f"Failed to create s3 client: {e}")
            raise

    def upload_file(self, file_path, object_name: None):
        """
        Upload a file s3 bucket
        :param file_path:
        :param object_name:
        :return:
        """
        if not os.path.exists(file_path):
            print(f"File not found:{file_path} ")
            return False
        if os.path.getsize(file_path) == 0:
            print(f"Empty file : {file_path}")
            return False
        object_name = object_name or os.path.basename(file_path)
        s3_key = f"{self.prefix}{object_name}"

        try:
            self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
            print(f"Successfully uploaded {file_path} to S3 as {s3_key}")
            return True

        except ClientError as e:
            print(f"Failed to upload {file_path} to s3: {e}")
            return False

    def upload_with_retry(self, file_path, max_retries=3, retry_delay=5, object_name=None):
        """
        upload file to s3 with retry
        :param file_path:
        :param max_retries:
        :param retry_delay:
        :return:
        """
        for attempt in range(max_retries):
            try:
                if self.upload_file(file_path,object_name):
                    return True
            except Exception as e:
                print(f"Upload attempt {attempt + 1} failed : {e}")

            if attempt < max_retries - 1:
                print(f"Retrying after {retry_delay} seconds")
                time.sleep(retry_delay)
        print(f"Failed to upload {file_path} after {retry_delay} attempts")
        return False


if __name__ == '__main__':
    try:
        uploader = S3Uploader()
        test_file = "data/transactions_20250717_224159.csv"
        if uploader.upload_with_retry(file_path=test_file):
            print("File uploaded successfully")
        else:
            print("file upload failed")
    except Exception as e:
        print(f"Failed to initialise s3 uploader: {e}")
