

import re
import datetime


#fileName_example = 'butt.jpgg  -date = 991017 -time = 20:10 -p=2  '
fileName_example = 'waffle.jpg -drinkDay = 1 -priority=4 -time = 20:10  -date = 991017'


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

        print 'found flags:\n'
        for f in items:
            print f[0]
        print '\n'


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
                    d = value
                    # print int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7])
                    d = datetime.date(int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7]))
                    print 'd = ', d
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
                    self.priority = int(value)
                except:
                    print 'invalid priority'
                    pass




print '\n\n** testing class ** \n\n'

newImage = ddParse(fileName_example)

print 'name: ', newImage.name
print 'drink day: ', newImage.drinkDay
print 'time: ', newImage.time
print 'date: ', newImage.date
print 'priority ', newImage.priority
