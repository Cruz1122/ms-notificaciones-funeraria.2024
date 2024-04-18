import os
import boto3

class cliData:
    def getClient():
        return boto3.client(
            "sns",
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            region_name="us-east-1",
        )
