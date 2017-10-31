import dd_parse as p
from datetime import datetime
import time
import os



found_images = [
    'poop.jpg -z=1 -p=3 t=10:12 -d=121019',
    'waffle.jpg --drinkDay=0 --priority=4 --time=20:10  --date=171030',
    'cat.jpg --date=171030',
    'dog.tif -z=1 --date=171030',
    'turtle.exr -p=1',
    #'catastrophe -p=10 --date=171030',
    #'calamaty -p=10 --date=171030',
    'dd1 -z=1',
    'dd2 -z=1',
    'dd3 -z=1',
    'dd4 -z=1',
    'dd5 -z=1',
    'dd6 -z=1',
    'dd7 -z=1',
    'dd8 -z=1',
    'dd9 -z=1',
    'nd1 -z=0',
    'nd2 -z=0',
    'nd3 -z=0',

    ]

def find_images(path):
    files = os.listdir(path)
    return files



print found_images

def today_is_drinkDay():
        return (datetime.now().timetuple().tm_yday)  % 2



path = './resources/images'
interval = 3600/4-1
sleep = 60
drink_day_invert = 0

delta = 0
daystate = today_is_drinkDay()
count = 0
last = None
while True:
    #images = find_images(path)
    images = found_images
    selection = p.select(p.score (images, (drink_day_invert) - today_is_drinkDay()))

    # first time, or if day changes
    if count == 0 or today_is_drinkDay() != daystate:
        last = selection
        then = datetime.now()
        daystate = today_is_drinkDay()
        print selection


    #all other times
    else:
        delta = int((datetime.now()-then).total_seconds())
        print delta, datetime.now().second
        print delta, interval
        print '\n'

        if delta > interval:
            then = datetime.now()

            if selection != last:

                print selection
                print datetime.now()
                print '\n'

                last = selection

    count +=1
    time.sleep(sleep)

