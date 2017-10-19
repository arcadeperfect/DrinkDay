#!/usr/bin/env python
import runtext_a
import imageLoader as il
import multiprocessing as mp
from rgbmatrix import RGBMatrix, RGBMatrixOptions

img1 = 'images/drink.png'
img2 = 'images/dontDrink.png'
brightness = 100

'''
def runTheText(text,colour):

    if __name__ == "__main__":
        run_text = runtext_a.RunText(text,colour)
        if (not run_text.process()):
            run_text.print_help()


#runTheText('farts', [10,50,40])
'''

if __name__ == '__main__':

    myQueue = mp.Queue()
    process1 = il.image_loader(myQueue)
    process1.start()

    myQueue.put(il.message(img1,10))
    #time.sleep(5)
    myQueue.put(il.message(img2,20))