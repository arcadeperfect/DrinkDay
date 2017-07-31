# https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python
# https://googlecloudplatform.github.io/google-cloud-python/stable/storage/client.html
# https://googlecloudplatform.github.io/google-cloud-python/stable/storage/blobs.html

from google.cloud import storage

client = storage.Client()
bucketName = "drinkday_images"
b = client.get_bucket(bucketName)

for i in b.list_blobs():
	print i
