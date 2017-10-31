import dd_parse as p
from datetime import datetime
import time
import os
from random import randint

path = './resources/images'
#print os.listdir(path)

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
    #'dd4 -z=1',
    #'dd5 -z=1',
    #'dd6 -z=1',
    #'dd7 -z=1',
    #'dd8 -z=1',
    #'dd9 -z=1',
    'nd1 -z=0',
    'nd2 -z=0',
    'nd3 -z=0',
    #'nd4 -z=0',
    #'nd5 -z=0',
    #'nd6 -z=0',
    #'nd7 -z=0',
    #'nd8 -z=0',
    #'nd9 -z=0'
    ]

def find_images(path):
    files = os.listdir(path)
    return files

found_images = find_images(path)

print found_images

def today_is_drinkDay():
        return (datetime.now().timetuple().tm_yday)  % 2

last = None
count = 0
delta = 0
interval = 3600/4
interval = 2
interval = interval-1
daystate = today_is_drinkDay()
drink_day_reverse = 0

while True:
    images = find_images(path)
    selection = p.select(p.score (images, (drink_day_reverse) - today_is_drinkDay()))

    # first time, or if day changes
    if count == 0 or today_is_drinkDay() != daystate:
        last = selection
        then = datetime.now()
        daystate = today_is_drinkDay()


    #all other times
    else:
        delta = int((datetime.now()-then).total_seconds())
        print delta, datetime.now().second

        if delta > interval:
            then = datetime.now()

            if selection != last:

                print selection

                last = selection

    count +=1
    time.sleep(1)

