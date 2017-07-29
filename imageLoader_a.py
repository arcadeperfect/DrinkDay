#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image


img = 'drink.png'


def imageLoader(img):
	print 'butttttttt'
	
	image = Image.open(img)
	options = RGBMatrixOptions()
	options.brightness = 40
	options.rows = 16
	options.chain_length = 1
	options.parallel = 1
	options.hardware_mapping = 'regular'
	matrix = RGBMatrix(options = options)
	matrix.SetImage(image.convert('RGB'))
	
	i = 0
	while i < 5:
		i += 1
		time.sleep(1)
		

#imageLoader(img)