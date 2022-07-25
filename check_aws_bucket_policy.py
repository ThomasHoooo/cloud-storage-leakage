import boto3
from botocore import UNSIGNED
from botocore.client import Config
import requests
import concurrent

def check_bucket_open(bucket_name):
    try:
        print(bucket_name)
        print(client.get_bucket_acl(Bucket=bucket_name))
        f.write(bucket_name+"\n")
    except Exception:
        pass

requests.urllib3.disable_warnings()
client = boto3.client('s3', config=Config(signature_version=UNSIGNED), verify=False)

with open('alexa_top_10k_aws_open_buckets.txt', 'r') as r, open('alexa_top_10k_aws_public_policy.txt', 'w+') as f:
    lines = r.readlines()
    with concurrent.futures.ThreadPoolExecutor(20) as executor:
        for line in lines:
            bucket = line.strip("\n").split(".")[0]
            executor.submit(check_bucket_open, bucket)
