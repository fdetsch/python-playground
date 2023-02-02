import boto3
import io
import pandas as pd

print('Loading function')

s3 = boto3.client(
    's3',
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
)

# read single parquet file from s3 (see https://stackoverflow.com/a/53900495)
def pd_read_s3_parquet(bucket, key, **args):
    obj = s3.get_object(Bucket = bucket, Key = key)
    return pd.read_parquet(io.BytesIO(obj['Body'].read()), **args)

bucket = 'makx-test-bucket'
key = 'N42@3034_W123@2230_2/year=2023/month=01/data-part-0.parquet'

def lambda_handler(event, context):
    
    try:
        parquet_data = pd_read_s3_parquet(bucket, key)
        print(parquet_data.head())
        return(parquet_data.head().to_json())
    except Exception as e:
        print(e)
        print('Error reading Parquet data from bucket {}. Make sure it exists and your bucket is in the same region as this function.'.format(bucket))
        raise e

'''
# debug (use `None` to avoid 'missing 2 required positional arguments' error):
lambda_handler(None, None)
'''
