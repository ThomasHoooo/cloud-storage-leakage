import boto3
from botocore.handlers import disable_signing

ADD_KEYWORDS = ["demo",
                "test",
                "dev",
                "mobile",
                "web",
                "app",
                "application",
                "api",
                "mobileapp",
                "staging",
                "prod",
                "production",
                "stage",
                "mock",
                "sd",
                "live",
                "uat",
                "qa",
                "user",
                "sand"]

with open('S&P top 500.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        s3 = boto3.resource('s3')
        s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
        bucket_name = line.strip("\n").split(".")[0]
        for keyword in ADD_KEYWORDS:
            enumerated_buckets = [f"{bucket_name}-{keyword}", 
                                f"{bucket_name}{keyword}",
                                f"{bucket_name}{keyword}123",
                                f"{keyword}{bucket_name}",
                                f"{bucket_name}-{keyword}",
                                f"{keyword}.{bucket_name}",
                                f"{keyword}-{bucket_name}"]
            for enumerated_bucket in enumerated_buckets:
                bucket = s3.Bucket(enumerated_bucket)
                try:
                    for object in bucket.objects.all():
                        #print(len(list(bucket.objects.all())))
                        print(bucket_name+".s3.amazonaws.com")
                        break
                except Exception:
                    pass