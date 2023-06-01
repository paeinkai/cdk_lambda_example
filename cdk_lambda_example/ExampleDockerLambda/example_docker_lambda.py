
import boto3
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image

s3_client = boto3.client('s3')

def resize_image(image_path, resized_path,size=768):
    with Image.open(image_path) as image:
        image.thumbnail((size,size))
        image.save(resized_path)

def handler(event, context):
    for record in event['Records']:
        upload_bucket = "neoart-training-data-thumbnail"
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        splitkey = key.split("/")
        new768key= "/".join(splitkey[:-1]) + "-thumbnail-768/" + splitkey[-1] 
        new256key= "/".join(splitkey[:-1]) + "-thumbnail-256/" + splitkey[-1] 
        tmpkey = key.replace('/', '')
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        upload_path_768 = '/tmp/resized768-{}'.format(tmpkey)
        upload_path_256 = '/tmp/resized256-{}'.format(tmpkey)
        print("bucket:",bucket),
        print("key:",key)
        s3_client.download_file(bucket, key, download_path)
        #resize to 768 thumbnail
        resize_image(download_path, upload_path_768, 768)
        s3_client.upload_file(upload_path_768, upload_bucket, new768key,ExtraArgs={'ACL': 'public-read'})
        print("upload_bucket:",upload_bucket)
        print("upload_key:",new768key)
        #resize to 256 thumbnail
        resize_image(download_path, upload_path_256, 256)
        s3_client.upload_file(upload_path_256, upload_bucket, new256key,ExtraArgs={'ACL': 'public-read'})
        
# import requests


# def handler(event, context):
#     return "Hello Lambda!"
