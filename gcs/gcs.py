"""
https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python
https://googlecloudplatform.github.io/google-cloud-python/stable/storage/client.html
https://googlecloudplatform.github.io/google-cloud-python/stable/storage/blobs.html
https://cloud.google.com/storage/docs/object-basics#download
"""


from google.cloud import storage
from os import listdir


def downloadNew(bucketName='drinkday_images', imagePath='./img'):
    bucket = storage.Client("DrinkDay").get_bucket(bucketName)
    for blob in bucket.list_blobs():
        if not blob.name in listdir(imagePath):
            print 'downloading %s' % blob.name
            blob.download_to_filename('./img/%s' % blob.name)


downloadNew()

