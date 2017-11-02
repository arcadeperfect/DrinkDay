import os
import time
import multiprocessing as mp
from datetime import datetime
from os import listdir

from google.cloud import storage

import dd_parse as p
from mtrx_image_loader import message, image_loader
#from display_image import display_image
import gcs


#from rgbmatrix import Adafruit_RGBmatrix


def today_is_drinkDay():
        return (datetime.now().timetuple().tm_yday)  % 2

bucket = 'drinkday_images'
project = "DrinkDay"
path = './resources/images'

interval = 1
sleep = 10
drink_day_invert = 1

delta = 0
daystate = today_is_drinkDay()
count = 0
last = None

queue = mp.Queue()
process = image_loader(queue)
process.start()



if __name__ == '__main__':
    #print 'started'
    #matrix = Adafruit_RGBmatrix(16, 1)



    while True:
        print count
        
        ## download images from google
        #downloadNew(bucket, path, project)
        #print '1'
        print 'downloading off google \n'
        gcs.downloadNew(bucket, path, project)

        ## list images on disk
        found_images = gcs.find_images(path)
        #print found_images
        #print '2'

        ## print found_images
        images = found_images
        print '\n\n\n** found images **\n '
        for i in found_images:
            print i
        print '\n ********\n'
        #print '3'

        ## do the sorting
        today_is_drinkDay_var = drink_day_invert-today_is_drinkDay()
        #today_is_drinkDay_variable = 0

        selection = p.select(p.score (images, today_is_drinkDay_var))

        #print 'selection: ', selection
        file = "%s/%s" %(path,selection[2])
        #print file

                ## first time, or if day changes
        if count == 0 or today_is_drinkDay() != daystate:
            print '\n***** first loop *****\n'
            last = selection
            then = datetime.now()
            daystate = today_is_drinkDay()
            print 'first time', file
            #display_image(path,selection[2])
            print 'displayed', file, '\n****\n'
            queue.put(message(file,-1))



        #all other times
        else:
            #print 'b'
            delta = int((datetime.now()-then).total_seconds())
            #print delta, datetime.now().second
            #print delta, interval
            

            if delta > interval:
                then = datetime.now()

                if selection != last:
                    #print 'c'

                    print '\n', '***** displayed *****', file, '\n****\n'
                    #display_image(path, selection[2])
                    #print datetime.now()
                    queue.put(message(file,-1))
                    last = selection

        count +=1
        #print count
        print 'count: ', count
        time.sleep(sleep)

