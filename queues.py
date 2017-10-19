import multiprocessing as mp


class message(object):

	def __init__(self, img, duration):
		self.img = img
		self.duration = duration


class display(mp.Process):

	def __init__(self, q):
		mp.Process.__init__(self)
		self.q = q

	def run(self):
		
		print 'running'
		while True:
			message = q.get()
			print message.img
			print message.duration



if __name__ == '__main__':
	queue = mp.Queue()

	
	queue.put(message('alex.png',10))

	q = mp.Queue()

	p1 = display(q)
	p1.start()

	#q.put('butt')
	q.put(message('drink.png',10))


