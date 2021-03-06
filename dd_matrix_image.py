
#!/usr/bin/env python

# handy info here
# https://pymotw.com/2/multiprocessing/communication.html
#from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import sys
from rgbmatrix import Adafruit_RGBmatrix
from PIL import Image
from PIL import ImageEnhance
import multiprocessing as mp
# import netTime

img1 = './resources/static_images/drink.png'
img2 = './resources/static_images/dontDrink.png'


# options = RGBMatrixOptions()
# options.brightness = 50
# options.rows = 16
# options.chain_length = 1
# options.parallel = 1
# options.hardware_mapping = 'regular'


class message(object):

    def __init__(self, img, duration):
        self.img = img
        self.duration = duration


class image_loader(mp.Process):

    def __init__(self, q):
        mp.Process.__init__(self)
        self.q = q

    def run(self):
        matrix = Adafruit_RGBmatrix(16, 1)
        #print 'running'
        while True:
            message = self.q.get()
            img = message.img
            dur = message.duration                        
            image = Image.open(img)
            image.load()
            #image = image.thumbnail((32, 16), Image.ANTIALIAS)

            enhancer = ImageEnhance.Brightness( image )
            image = enhancer.enhance( 0.5 )

            matrix.SetImage(image.im.id)
            if dur >= 0:
                time.sleep(dur)
                matrix.Clear()



q = mp.Queue()
c = 0 



from random import randint
import gcs
path = './resources/images'

if __name__ == '__main__':

    q = mp.Queue()
    p1 = image_loader(q)
    p1.start()


    while True:

        found_images = gcs.find_images(path)

        print c
        if c % 10 == 0:
            print 'printing'
            file = [img1,img2][randint(0,1)]
            q.put(message(file,-1))
        else:
            print 'didnt'

        c += 1

        time.sleep(1)



