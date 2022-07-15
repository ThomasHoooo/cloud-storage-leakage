import boto3
from botocore import UNSIGNED
from botocore.client import Config
import requests
import concurrent

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
    try:
        print(bucket_name)
        for key in client.list_objects(Bucket=bucket_name)['Contents']:
            print(bucket_name+ ".s3.amazonaws.com")
            f.write(bucket_name + ".s3.amazonaws.com\n")
            break
    except Exception:
        pass

requests.urllib3.disable_warnings()
client = boto3.client('s3', config=Config(signature_version=UNSIGNED), verify=False)

with open('alexa_top_10k.txt', 'r') as r, open('alexa_top_10k_aws_open_buckets.txt', 'w+') as f:
    lines = r.readlines()
    with concurrent.futures.ThreadPoolExecutor(20) as executor:
        for line in lines:
            website_name = line.strip("\n").split(",")[1].removeprefix("www.").split(".")[0]
            executor.submit(check_bucket_open, website_name)
            for keyword in ADD_KEYWORDS:
                enumerated_buckets = [f"{website_name}-{keyword}", 
                                    f"{website_name}{keyword}",
                                    f"{keyword}{website_name}",
                                    f"{keyword}.{website_name}",
                                    f"{keyword}-{website_name}"]
                executor.map(check_bucket_open, enumerated_buckets)
