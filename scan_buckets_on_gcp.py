from google.cloud import storage


with open('S&P top 500.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        storage_client = storage.Client.create_anonymous_client()
        bucket_name = line.strip("\n").split(".")[0]
        for blob in list(storage_client.bucket(bucket_name).list_blobs()):
            try:
                curr = blob.name
                print(bucket_name+".blob.core.windows.net")
                break
            except Exception:
                pass