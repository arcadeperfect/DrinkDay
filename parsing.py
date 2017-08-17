"""
https://docs.python.org/3/howto/regex.html
https://codereview.stackexchange.com/questions/86235/parsing-a-big-text-file-extract-data-store-it-in-a-csv-file
"""

import re
import datetime


fileName = 'butt.jpgg  -date = 991017 -time = 20:10 -p=2  '
#fileName = 'butt.jpg'
fileName = re.sub('[\s+]', '', fileName)

parsed ={}
parsed = dict(name=fileName.split('-')[0])

def file_parse(fileName):
    validFlags = ['d', 'date', 'time', 'p']

    print '\n parsing\n'

    for i in fileName.split('-')[1:]:

        try:
            flag = i.split('=')[0]
            value = i.split('=')[1]

            if flag in validFlags:

                if flag == 'date':
                    try:
                        d = value
                        print int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7])
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

                elif flag == 'd':
                    if value == '1':
                        parsed['drink_day'] = True
                    if value == '0':
                        parsed['drink_day'] = False

                else:
                    try:
                        parsed[flag] = int(value)
                    except:
                        parsed[flag] = value

            else:
                print '"%s" is an invalid flag \n'
        except:
            print 'failed to split "%s" on = \n' %i

    if len(parsed.keys()) == 1:
        parsed['misc'] = True

    return parsed

file_parse(fileName)


print '\n\nprinting dict \n'

for i in parsed.keys():
    print i, ':', parsed[i]



class dd_image:
    def __init__(self, file, name, drink_day, time, date, priority):
        self.file = file
        self.name = name
        self.drink_day = drink_day
        self.time = time
        self.date = date
        self.priority = priority

    validFlags = ['d', 'date', 'time', 'p']

    def parse(self):
        print '\n parsing\n'

        for i in file.split('-')[1:]:

            try:
                flag = i.split('=')[0]
                value = i.split('=')[1]

                if flag in validFlags:

                    if flag == 'date':
                        try:
                            d = value
                            print int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7])
                            d = datetime.date(int(d[0:2]) + 2000, int(d[2:4]), int(d[4:7]))

                            parsed[flag] = d

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

                    elif flag == 'd':
                        if value == '1':
                            parsed['drink_day'] = True
                        if value == '0':
                            parsed['drink_day'] = False

                    else:
                        try:
                            parsed[flag] = int(value)
                        except:
                            parsed[flag] = value

                else:
                    print '"%s" is an invalid flag \n'
            except:
                print 'failed to split "%s" on = \n' % i

        if len(parsed.keys()) == 1:
            parsed['misc'] = True

        return parsed