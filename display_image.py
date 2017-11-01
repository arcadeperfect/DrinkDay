from PIL import Image
import gcs
import time
path = './resources/images'

def display_image(location,image):
    if image[0] != '.':
        Image.open('%s/%s' %(location,image)).show()
    else:
        print "was a hidden file"



#
# for i in gcs.find_images(path):
#     display_image(path,i)