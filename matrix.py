import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix
import inspect
#from rgbmatrix import RGBMatrixOptions

matrixx = Adafruit_RGBmatrix(16, 1, brightness=100)
path ="./resources/static_images"

# options = RGBMatrixOptions()
# options.brightness = 50
# options.rows = 16
# options.chain_length = 1
# options.parallel = 1
# options.hardware_mapping = 'regular'


def matrixLoad(file, matrix):
	matrix.Clear()
	image = Image.open(file)
	image.load()

	matrix.SetImage(image.im.id)
	time.sleep(4)
	

file = "%s/%s" %(path, 'drink.png')

print file

if __name__ == '__main__':

	matrixLoad(file, matrixx)



#matrixx.Clear()