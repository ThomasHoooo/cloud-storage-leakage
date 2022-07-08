import boto3
from botocore.handlers import disable_signing
import concurrent.futures

ADD_KEYWORDS = ["demo",
                "test",
                "dev",
                "web",
                "app",
                "application",
                "api",
                "staging",
                "prod",
                "production",
                "stage",
                "mock",
                "live",
                "user"]

def check_bucket_open(bucket_name):
    bucket = s3.Bucket(bucket_name)
    try:
        for object in bucket.objects.all():
            f.write(bucket.name + ".s3.amazonaws.com\n")
            print(bucket.name)
            break
    except Exception:
        pass

s3 = boto3.resource('s3')
s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
public_buckets = []

with open('alexa_top_10k.txt', 'r') as r, open('alexa_top_10k_aws_open_buckets.txt', 'w+') as f:
    lines = r.readlines()
    with concurrent.futures.ThreadPoolExecutor(20) as executor:
        for line in lines:
            website_name = line.strip("\n").split(",")[1].split(".")[0]
            executor.submit(check_bucket_open, website_name)
            for keyword in ADD_KEYWORDS:
                enumerated_buckets = [f"{website_name}-{keyword}", 
                                    f"{website_name}{keyword}",
                                    f"{keyword}{website_name}",
                                    f"{keyword}.{website_name}",
                                    f"{keyword}-{website_name}"]
                executor.map(check_bucket_open, enumerated_buckets)
