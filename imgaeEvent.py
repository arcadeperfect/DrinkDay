import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import multiprocessing as mp


def willy(e):
	print 'waiting'
	e.wait()







if __name__ == '__main__':
	e = mp.Event()
	p1 = mp.Process(name='block', target = willy,)