from PIL import Image
import os


import time
path = './resources/images'


def screenShow(image, mult = 20):
    try:
        print image[0]
        loadedImage = Image.open(image)
        loadedImage = loadedImage.resize((32*mult,16*mult))
        loadedImage.show()
        #Image.open('%s/%s' %(location,image)).thumbnail((16*mult, 32*mult)).show()
    except:
        print("failed to display image")




# for i in os.listdir(path):
#     if i != '.' or i != '..':
#         display_image(path,i)
#
# display_image(path, 'drink.png -z=1')
#
#
#
