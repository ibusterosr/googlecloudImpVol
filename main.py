import json
import numpy as np
from google.cloud import storage
import datetime
import os

def suma(a,b):

    resultado = a+b
    return resultado

def create_dict(request):
    dicc = {}
    for i in range(10):
        n_array = []
        for j in range(10):
            a1=np.random.randint(low=0,high=10)
            a2=np.random.randint(low=0,high=10)
            n_array.append(suma(a1,a2))
        dicc[i] = n_array

    # Get the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    # Define the filename using the current time
    filename = f"dict_{current_time}.json"

    # Get the GCS bucket
    bucket_name = 'storagesuma12'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f'final/{filename}')
    dicc_str = json.dumps(dicc)
    blob.upload_from_string(dicc_str)


    # Devolvemos el diccionario
    return dicc_str