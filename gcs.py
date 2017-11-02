"""
https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python
https://googlecloudplatform.github.io/google-cloud-python/stable/storage/client.html
https://googlecloudplatform.github.io/google-cloud-python/stable/storage/blobs.html
https://cloud.google.com/storage/docs/object-basics#download
"""


from google.cloud import storage
from os import listdir

path = './resources/images'
bucket = 'drinkday_images'
project = "DrinkDay"

def downloadNew(bucketName, imagePath, project):
    bucket = storage.Client(project).get_bucket(bucketName)
    for blob in bucket.list_blobs():
        if not blob.name in listdir(imagePath):
            print 'downloading %s' % blob.name
            blob.download_to_filename('%s/%s' % (path,blob.name))

def find_images(path):
    files = [x for x in listdir(path) if x[0]!='.']
    return files
#downloadNew(bucket,path,project)

if __name__ == '__main__':
	downloadNew(bucket, path, project)