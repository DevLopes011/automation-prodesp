import boto3
import re, os
#from utils.RegexPattern import PATTERN
from dotenv import load_dotenv

class AwsManager:         
    def __init__(self):
        # sqs = boto3.resource('sqs')
        # load_dotenv()
        # self.aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
        # self.aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        # self.s3_region_name = os.environ.get("S3_REGION_NAME")
        # self.bucket_name_input = os.environ.get("BUCKET_NAME_INPUT")
        pass
        
    def upload_dynamo (self):
        boto3.setup_default_session(profile_name="ah")
        dynamodb_client = boto3.client("dynamodb")
        table_name = "automations"
        response = dynamodb_client.put_item(
            TableName=table_name,
            Item={
                "order_id": {"S": "ord1234"},
                "order_date": {"S": "2022-08-03"},
                "user_email": {"S": "test@example.com"},
                "amount": {"N": "120"},
            },
        )
        print(response)
        
awsManager = AwsManager()
awsManager.upload_dynamo()