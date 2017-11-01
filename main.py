import dd_parse as p
from datetime import datetime
import time
import os
import gcs
from display_image import display_image

from mtrx_image_loader import message, image_loader
import multiprocessing as mp

def today_is_drinkDay():
        return (datetime.now().timetuple().tm_yday)  % 2

bucket = 'drinkday_images'
project = "DrinkDay"

path = './resources/images'
interval = 1
sleep = 5
drink_day_invert = 1

delta = 0
daystate = today_is_drinkDay()
count = 0
last = None


if __name__ == '__main__':
    #print 'started'

    queue = mp.Queue()
    process = image_loader(queue)
    process.start()


    while True:
        print count
        #print 'in loop'

        ## download images from google
        #gcs.downloadNew(bucket, path, project)
        #print '1'

        ## list images on disk
        found_images = gcs.find_images(path)
        #print '2'

        ## print found_images
        images = found_images
        #print '3'

        ## do the sorting
        selection = p.select(p.score (images, (drink_day_invert) - today_is_drinkDay()))

        #print 'selection: ', selection
        file = "%s/%s" %(path,selection[2])
        #print file

        ## first time, or if day changes
        if count == 0 or today_is_drinkDay() != daystate:
            last = selection
            then = datetime.now()
            daystate = today_is_drinkDay()
            print 'first time', file
            #display_image(path,selection[2])
            queue.put(message(file,5))



        #all other times
        else:
            delta = int((datetime.now()-then).total_seconds())
            #print delta, datetime.now().second
            #print delta, interval
            

            if delta > interval:
                then = datetime.now()

                if selection != last:

                    print file
                    #display_image(path, selection[2])
                    #print datetime.now()
                    queue.put(message(file,5))
                    last = selection

        count +=1
        #print count
        time.sleep(sleep)

