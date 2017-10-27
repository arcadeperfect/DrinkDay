print '\n\n'


"""
https://docs.python.org/3/howto/regex.html
https://codereview.stackexchange.com/questions/86235/parsing-a-big-text-file-extract-data-store-it-in-a-csv-file
"""

import re
import datetime


fileName_example = 'butt.jpgg  -date = 991017 -time = 20:10 -p=2  '
fileName_example = 'waffle.jpg -drinkDay = 1 -priority=4 -time = 20:10, date = 991017'
#fileName_example = 'smellbags.exr -agfesgergs'



def file_parse(fileName):

    print '\n ___parsing___\n'

    #remove spaces
    fileName = re.sub('[\s+]', '', fileName).lower()

    #create dict
    parsed = dict(name=fileName.split('-')[0])

    #acceptable flags
    validFlags = ['drinkday', 'date', 'time', 'p']


    for i in fileName.split('-')[1:]:

        try:
            flag = i.split('=')[0]
            value = i.split('=')[1]
            #print i, flag, value

            if flag in validFlags:

                if flag == 'date':
                    try:
                        d = value
                        #print int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7])
                        d = datetime.date(int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7]))

                        parsed[flag]= d

                    except:
                        print 'invalid date'
                        pass

                elif flag == 'time':
                    try:
                        t = [int(t) for t in value.split(':')]
                        t = datetime.time(t[0], t[1])
                        parsed[flag] = t

                    except:
                        print 'invalid time'
                        pass

                elif flag == 'p':
                    parsed['priority'] = value

                elif flag == 'drinkday':


                    if value == '1' or value == 'True':
                        parsed['drink_day'] = True
                    if value == '0' or value == "False":
                        parsed['drink_day'] = False

                else:
                    try:
                        parsed[flag] = int(value)
                    except:
                        parsed[flag] = value

            else:
                print '%s is an invalid flag \n' %flag
        except:
            print 'failed to split "%s" on = \n' %i



    return parsed


class ddParse:
    def __init__(self, fileName, name = None, drinkDay = 0, date = None, time = None, priority = None):
        self.fileName = fileName
        self.drinkDay = drinkDay
        self.date = date
        self.time = time
        self.priority = priority

        # remove spaces
        fileName = re.sub('[\s+]', '', fileName)

        items = [f.split("=") for f in fileName.split('-')]

        # first entry is always the name
        self.name = items[0][0]



        for item in items[1:]:

            flag = item[0]
            value = item[1]

            if flag == 'drinkDay':
                try:
                    self.drinkDay = int(value)
                except:
                    print 'invalid drinkday flag'
                    pass


            if flag == 'date':
                try:
                    d = flag[1]
                    # print int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7])
                    d = datetime.date(int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7]))
                    self.date = d

                except:
                    print 'invalid date'
                    pass


            if flag == 'time':
                try:
                    t = [int(t) for t in value.split(':')]
                    t = datetime.time(t[0], t[1])
                    self.time = t

                except:
                    print 'invalid time'
                    pass

            if flag == 'priority':
                try:
                    self.drinkDay = int(value)
                except:
                    print 'invalid priority'
                    pass






newImage = ddParse(fileName_example)



print '\n\n testing class \n\n'

print 'name: ', newImage.name
print 'drink day: ', newImage.drinkDay
print 'time: ', newImage.time
print 'date: ', newImage.date
print 'priority ', newImage.priority



# class ddParse:
#     def __init__(self, fileName, name,  drinkday, time, p):
#         self.fileName = fileName
#         self.name = name
#         self.drinkday = drinkday
#         self.time = time
#         self.p = p
