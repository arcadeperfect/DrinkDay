import datetime
import ntplib
import time
import os

client = ntplib.NTPClient()
response = client.request('pool.ntp.org', version=3)

#print response.offset

'''
to deliberately set the system time wrong for testing purposes:

sudo date -s "Thu Aug  9 21:31:26 UTC 2012"
'''

'''
print "system time \n"
print datetime.datetime.now()
print "\n"

print "ntplib time \n"
print response.tx_time
print time.ctime(response.tx_time)
print '\n'
'''

### Set system time

def setTime():
	print 'setting system time'
	os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
	
setTime()