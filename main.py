import dd_parse as p
from datetime import datetime
import time
import os
import gcs
from display_image import display_image



# found_images = [
#     'poop.jpg -z=1 -p=3 t=10:12 -d=121019',
#     'waffle.jpg --drinkDay=0 --priority=4 --time=20:10  --date=171030',
#     'cat.jpg --date=171030',
#     'dog.tif -z=1 --date=171030',
#     'turtle.exr -p=1',
#     #'catastrophe -p=10 --date=171030',
#     #'calamaty -p=10 --date=171030',
#     'dd1 -z=1',
#     'dd2 -z=1',
#     'dd3 -z=1',
#     'dd4 -z=1',
#     'dd5 -z=1',
#     'dd6 -z=1',
#     'dd7 -z=1',
#     'dd8 -z=1',
#     'dd9 -z=1',
#     'nd1 -z=0',
#     'nd2 -z=0',
#     'nd3 -z=0',
#
#     ]

def today_is_drinkDay():
        return (datetime.now().timetuple().tm_yday)  % 2

bucket = 'drinkday_images'
project = "DrinkDay"

path = './resources/images'
interval = 1
sleep = 1
drink_day_invert = 1

delta = 0
daystate = today_is_drinkDay()
count = 0
last = None

print 'starting'

while True:

    #download images from google
    gcs.downloadNew(bucket, path, project)

    #list images on disk
    found_images = gcs.find_images(path)
    #print found_images
    images = found_images

    #do the sorting
    selection = p.select(p.score (images, (drink_day_invert) - today_is_drinkDay()))

    # first time, or if day changes
    if count == 0 or today_is_drinkDay() != daystate:
        last = selection
        then = datetime.now()
        daystate = today_is_drinkDay()
        print 'first time', selection
        display_image(path,selection[2])


    #all other times
    else:
        delta = int((datetime.now()-then).total_seconds())
        #print delta, datetime.now().second
        #print delta, interval
        print '\n'

        if delta > interval:
            then = datetime.now()

            if selection != last:

                print selection
                display_image(path, selection[2])
                #print datetime.now()
                print '\n'

                last = selection

    count +=1
    print count
    time.sleep(sleep)

