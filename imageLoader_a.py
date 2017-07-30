#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
from multiprocessing import Process
from multiprocessing import Queue

img1 = 'drink.png'
img2 = 'alex.png'

def loadImage(img, q):
    #img = 'drink.png'
    img2='alex.png'
    options = RGBMatrixOptions()
    options.brightness = 10
    options.rows = 16
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'regular'
    matrix = RGBMatrix(options = options)
    image = Image.open(img)
    matrix.SetImage(image.convert('RGB'))
    while True:
        message = q.get()
        print message
        if message == 'quit':
            image = Image.open(img2)
            matrix.SetImage(image.convert('RGB'))
        #time.sleep(1)
        

if __name__ == '__main__':

    myQueue = Queue()


    p1 = Process(target=loadImage, args=(img1, myQueue))
    p1.start()
    
    x = 0

    while True:
        time.sleep(0.5)
        myQueue.put('qtest')
        x += 1
        if x > 5:
            myQueue.put('quit')

    

