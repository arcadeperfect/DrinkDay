#!/usr/bin/env python
import runtext_a
from imageLoader_a import imageLoader

img = 'drink.png'
brightness = 100

def runTheText(text,colour):

    if __name__ == "__main__":
        run_text = runtext_a.RunText(text,colour)
        if (not run_text.process()):
            run_text.print_help()






#runTheText('farts', [10,50,40])

while True:
	imageLoader(img, brightness, 10)