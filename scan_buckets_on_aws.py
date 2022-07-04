import boto3
from botocore.handlers import disable_signing

with open('S&P top 500.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        s3 = boto3.resource('s3')
        s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
        bucket_name = line.strip("\n").split(".")[0]
        bucket = s3.Bucket(bucket_name)
        try:
            print(len(list(bucket.objects.all())))
            print(bucket_name+".s3.amazonaws.com")
        except Exception:
            pass