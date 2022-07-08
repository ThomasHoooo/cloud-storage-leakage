from google.cloud import storage
storage_client = storage.Client.create_anonymous_client()
bucket_name = "testunity"
for blob in list(storage_client.bucket(bucket_name).list_blobs()):
    curr = blob.name
    print(bucket_name)
    break