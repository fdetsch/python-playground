import boto3
import os

print('Loading function')

s3 = boto3.client(
    's3',
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
)

def lambda_handler(event, context):
    
    buckets = s3.list_buckets()

    bucket_names = []
    for bucket in buckets['Buckets']:
        bucket_names.append(bucket.get('Name'))
    
    return(bucket_names)

'''
# debug (use `None` to avoid 'missing 2 required positional arguments' error):
lambda_handler(None, None)
'''
