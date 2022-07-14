from google.cloud import storage
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
    try:
        print(bucket_name)
        for blob in list(storage_client.bucket(bucket_name).list_blobs()):
            curr = blob.name
            f.write(bucket_name+".storage.googleapis.com\n")
            print(bucket_name)
            break
    except Exception as e:
        pass

storage_client = storage.Client.create_anonymous_client()
final_results = []

with open('alexa_top_10k.txt', 'r') as r, open('alexa_top_10k_gcp_open_buckets.txt', 'w+') as f:
    with concurrent.futures.ThreadPoolExecutor(10) as executor:
        for line in r:
            bucket_name = line.strip("\n").split(",")[1].split(".")[0]
            executor.submit(check_bucket_open, bucket_name)
            for keyword in ADD_KEYWORDS:
                enumerated_buckets = [f"{bucket_name}-{keyword}", 
                                    f"{bucket_name}{keyword}",
                                    f"{keyword}{bucket_name}",
                                    f"{keyword}.{bucket_name}",
                                    f"{keyword}-{bucket_name}",
                                    ]
                executor.map(check_bucket_open, enumerated_buckets)

                