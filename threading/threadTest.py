import time
import threading
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s %(threadName)s] %(message)s',
                    datefmt='%H:%M:%S')

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()
    #logger.info('test')

    def run(self):
        logger.info('test')

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

bum = StoppableThread.start()

