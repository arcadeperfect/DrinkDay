#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

'''
def loadImage():
	print 'butt'
	img = 'drink.png'
	image = Image.open(img)

	# Configuration for the matrix
	options = RGBMatrixOptions()
	options.rows = 16
	options.chain_length = 1
	options.parallel = 1
	options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
	options.brightness = 50
	matrix = RGBMatrix(options = options)

	# Make image fit our screen.
	#image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

	matrix.SetImage(image.convert('RGB'))

	print 'butt'
'''

img = 'drink.png'
image = Image.open(img)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 16
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.brightness = 50
matrix = RGBMatrix(options = options)

# Make image fit our screen.
#image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'))


while True:
	time.sleep(100)