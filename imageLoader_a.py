#!/usr/bin/env python
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
from multiprocessing import Process

img1 = 'drink.png'
img2 = 'alex.png'

def loadImage():
    img = 'drink.png'
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
        print 'butt'
        time.sleep(0.5)


if __name__ == '__main__':
    p1 = Process(target=loadImage,)
    p1.start()
    #p2 = Process(target=loadImage, args=(img2),)
    #p2.start()
    print 'butts'
    time.sleep(5)
    print 'big butts'
    p1.terminate()
    time.sleep(3)
