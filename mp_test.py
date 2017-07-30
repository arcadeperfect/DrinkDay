from multiprocessing import Pool
from multiprocessing import Process
import time

def f(name):
    while True:
    	print name
    	time.sleep(1)

def g(name):
    while True:
    	print name
    	time.sleep(2)


print 'c'

if __name__ == '__main__':
    p1 = Process(target=f, args=('bob',))
    p1.start()
    p2 = Process(target=g, args=('james',))
    p2.start()
    #p.join()