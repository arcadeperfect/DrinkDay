#!/usr/bin/env python

# handy info here
# https://pymotw.com/2/multiprocessing/communication.html
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import multiprocessing as mp
import netTime

img1 = 'images/drink.png'
img2 = 'images/dontDrink.png'
img3 = 'images/cat1.jpg'
img4 = 'images/cat2.jpg'
img5 = 'images/dontDrink.png'

options = RGBMatrixOptions()
options.brightness = 50
options.rows = 16
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'


class message(object):

    def __init__(self, img, duration):
        self.img = img
        self.duration = duration


class image_loader(mp.Process):

    def __init__(self, q):
        mp.Process.__init__(self)
        self.q = q

    def run(self):
        matrix = RGBMatrix(options = options)
        print 'running'
        while True:
            message = q.get()
            img = message.img
            dur = message.duration                        
            image = Image.open(img)
            image.thumbnail((32, 16), Image.ANTIALIAS)
            matrix.SetImage(image.convert('RGB'))
            if dur >= 0:
                time.sleep(dur)
                matrix.Clear()



q = mp.Queue()

if __name__ == '__main__':

    q = mp.Queue()
    p1 = image_loader(q)
    p1.start()


    '''
    q.put(message(img1,1))
    #time.sleep(5)
    q.put(message(img3,5))

    q.put(message(img5,-1))

    #q.put(message(img5,20))
    '''
    print netTime.oddDay()
    while True:
        if netTime.oddDay() == True:
            print 'tru'
            q.put(message(img1,-1))

        elif netTime.oddDay() == False:
            print 'flse'
            q.put(message(img2,-1))
        time.sleep(1)




