"""
https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python
https://googlecloudplatform.github.io/google-cloud-python/stable/storage/client.html
https://googlecloudplatform.github.io/google-cloud-python/stable/storage/blobs.html
https://cloud.google.com/storage/docs/object-basics#download
"""

from google.cloud import storage
from os import listdir, remove

path = './resources/images'
bucket = 'drinkday_images'
project = "DrinkDay"


def download_new(bucket_name, image_path, project):
    bucket = storage.Client(project).get_bucket(bucket_name)
    for blob in bucket.list_blobs():
        if not blob.name in listdir(image_path):
            print '\n    downloading %s' % blob.name
            blob.download_to_filename('%s/%s' % (path, blob.name))


def delete_local(bucket_name, image_path, project):
    bucket = storage.Client(project).get_bucket(bucket_name)
    remoteList = [str(blob.name) for blob in bucket.list_blobs()]
    localList = listdir(image_path)
    for file in localList:
        if not file in remoteList:
            print '\n    removing: ', file
            remove('%s/%s' % (path, file))


def google_sync(bucket_name, image_path, project):
    download_new(bucket_name, image_path, project)
    delete_local(bucket_name, image_path, project)


def find_downloaded_images(path):
    files = [x for x in listdir(path) if x[0] != '.']
    return files


if __name__ == '__main__':
	google_sync(bucket, path, project)
