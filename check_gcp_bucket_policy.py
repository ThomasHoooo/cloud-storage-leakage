from google.cloud import storage
import concurrent.futures

def check_bucket_open(bucket_name):
    print(bucket_name)
    try:
        storage_client.bucket(bucket_name).get()
        f.write(bucket_name+" public metadata\n")
    except:
        pass
    try:
        storage_client.bucket(bucket_name).get_iam_policy(requested_policy_version=3)
        f.write(bucket_name+" public iam policy\n")
    except:
        pass

storage_client = storage.Client.create_anonymous_client()
final_results = []

with open('alexa_top_10k_gcp_open_buckets.txt', 'r') as r, open('alexa_top_10k_gcp_public_policy.txt', 'w+') as f:
    with concurrent.futures.ThreadPoolExecutor(10) as executor:
        for line in r:
            bucket_name = line.strip("\n").split(".")[0]
            executor.submit(check_bucket_open, bucket_name)

                