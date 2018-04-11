import argparse
import shlex
import datetime
from random import randint
from os import listdir

path = "./resources/images"

def find_images(path):
    files = [x for x in listdir(path) if x[0]!='.']
    return files

def date_to_object(date_string):
    try:
        date = datetime.date(int(date_string[0:2]) + 2000, int(date_string[2:4]), int(date_string[4:7]))
        return date
    except:
        #print "i really hated your date string: ", date_string
        return None

def time_to_object(time_string):
    try:
        t = [int(t) for t in time_string.split(':')]
        t = datetime.time(t[0], t[1])
        return t
    except:
        #print "i really hated your time string:", time_string
        return None

def parse(file_name):

    argument_list = shlex.split(file_name)
    #print argument_list
    parser = argparse.ArgumentParser(description='drinkDay parser')
    parser.add_argument('-z', '--drinkDay', type=int)
    parser.add_argument('-p', '--priority', type=int)
    parser.add_argument('-t', '--time')
    parser.add_argument('-d', '--date')

    options = parser.parse_known_args(argument_list)[0]
    #print "found options: ", options
    name = argument_list[0]
    #print "name" ,name

    img ={
        'name':name,
        'drinkDay':options.drinkDay,
        'priority':options.priority,
        'date': date_to_object(options.date),
        'time': time_to_object(options.time),
        'file': file_name
        }
    #print img
    return img


### Tests

# found_images = [
#     'poop.jpg -z=1 -p=3 t=10:12 -d=121019',
#     'waffle.jpg --drinkDay=0 --priority=4 --time=20:10  --date=991017',
#     'cat.jpg -z=0 -p=30',
#     'dog.tif -z=0',
#     'turtle.exr -z=1 -t=3 -d=1'
#     ]


def score(found_images,today_is_drinkDay):

    ranking = {}
    rankingList = []
    print '\n'

    for image in found_images:
        parsed_image = parse(image)
        name = parsed_image['name']
        drink_day = parsed_image['drinkDay']
        date = parsed_image['date']
        file = image
        #print 'file', file
        # if date == datetime.date.today():
        #     print 'matched date', name, date
            
        if drink_day == today_is_drinkDay:
            score = 3
            ranking[name] = [name,score,file]

        if drink_day == None:
            score = 1
            ranking[name] = [name, score,file]

        if date == datetime.date.today():
            print 'matched date: '

            score = 5
            print name, score, file
            ranking[name] = [name,score,file]
            print ranking[name]
            print '***************************'

    print ranking

    for i in ranking.keys():
        print 'in ranking:', ranking[i]
        rankingList.append([ranking[i][1], ranking[i][0], ranking[i][2]])
    #print rankingList
    print '\n'

    return sorted(rankingList)[::-1]


def select(scored_images):
    
    highest_score = scored_images[0][0]
    print "highest score is: ", highest_score
    selection_pool = []
    for i in scored_images:
        if i[0] == highest_score:
            selection_pool.append(i)
    randomIndex = randint(0,len(selection_pool)-1)
    return selection_pool[randomIndex]



if __name__ == '__main__':

    images = find_images(path)

    print '\n\n ***** test ***** \n\n'

    scored = score(images,0)

    print select(scored)

    # for i in score(images,1):
    #     print i
    #selection = select(score (images,1))

    #print selection


    #found_images = find_images(path)
    #print found_images
    #image_list = []

    # for i in found_images:
    #     image_list.append (parse(i))


    #for i in image_list:
        #print i['name'], i['drinkDay'], i['priority'], i['date'], i['time']
