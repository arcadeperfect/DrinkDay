"""
https://docs.python.org/3/howto/regex.html
https://codereview.stackexchange.com/questions/86235/parsing-a-big-text-file-extract-data-store-it-in-a-csv-file
"""

import re
import datetime

validFlags=['d', 'date', 'time', 'p']
fileName = 'drink.png -d=0 -date=990618 -time=12:10 -p=10 -fwqf '
fileName = re.sub('[\s+]', '', fileName)



parsed = {'name': fileName.split('-')[0]}

for i in fileName.split('-')[1:]:

    try:
        flag = i.split('=')[0]
        value = i.split('=')[1]

        if flag in validFlags:

            if flag == 'date':
                print 'flag is date'
                try:
                    t = value
                    d = datetime.date(int(t[0:2]) + 2000, int(t[2:4]), int(t[4:7]))
                    print 'date', d
                    parsed[flag] = d

                except:
                    print 'invalid date'
                    pass

            if flag == 'time':
                try:
                    t = datetime.time(hour=int(value.split(':')[0]),minute=int(value.split(':')[1]))
                    print 't', t
                    parsed[flag] = t

                except:
                    print 'invalid time'
                    pass


            else:
                try:
                    parsed[flag] = int(value)
                except:
                    parsed[flag] = value

        else:
            print '"%s" is an invalid flag \n'
    except:
        print 'failed to split "%s" on = \n' %i


for i in  parsed.keys():
    print i, parsed[i]


    #else:
        #print "%s is invalid flag" %flag

#print parsed



"""
p = re.compile('[a-z]+')

m = p.match('tempo')

print m.group()
print m.start(), m.end()
print m.span()
"""


"""
p = re.compile('[a-z]+')
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
"""


"""
p = re.compile('[a-z]+')
f = p.findall('string goes here')
if f:
    print f
else:
    print('No Match')
"""


"""
p = re.compile('\d+')
f = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
if f:
    print f
else:
    print('No Match')
"""



"""

iterator = p.finditer('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')

for match in iterator:
    print match.span()
"""


"""
#Module level functions
print(re.match(r'From\s+', 'Fromage amk'))

print re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
"""

"""
#groups

p = re.compile('(a(b)c)d')
m = p.match('abcd')
print m.group(0)

print m.group(1)

print m.group(2)
"""

