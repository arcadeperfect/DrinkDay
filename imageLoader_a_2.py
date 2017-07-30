#!/usr/bin/env python

# handy info here
# https://pymotw.com/2/multiprocessing/communication.html
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import multiprocessing as mp

img1 = 'drink.png'
img2 = 'alex.png'

options = RGBMatrixOptions()
options.brightness = 70
options.rows = 16
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'


class message(object):

    def __init__(self, img, duration):
        self.img = img
        self.duration = duration


class display(mp.Process):

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
            matrix.SetImage(image.convert('RGB'))
            time.sleep(dur)
            matrix.Clear()



if __name__ == '__main__':

    q = mp.Queue()
    p1 = display(q)
    p1.start()
    q.put(message('drink.png',1))
    #time.sleep(5)
    q.put(message('alex.png',20))




