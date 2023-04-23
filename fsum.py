from google.cloud import storage

def suma(request):
    a1 = 1
    a2 = 2
    result = a1 + a2

    storage_client = storage.Client()
    bucket = storage_client.bucket('storagesuma12')
    file = bucket.blob('result.txt')
    file.upload_from_string(str(result))

    return f'Result saved to {file.name}'