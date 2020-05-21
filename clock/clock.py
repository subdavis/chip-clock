import time
import math
import signal
import sys
import queue
from multiprocessing.dummy import Pool, Queue, Event

class ClockMode:
    def __init__(self, name, formatter):
        self.name = name
        self.formatter = formatter

    def run(self, event, queue):
        while not event.wait(timeout=0.5):
            self.value = time.time()
            queue.put({
                'name': self.name,
                'value': self.formatter(self.value),
            })

class DisplayDriver:
    def __init__(self, modes, renderers):
        self.currentMode = None
        self.modes = modes
        self.renderers = renderers
        self.event = Event()

    def signal_handler(self, sig, frame):
        print('SIGINT')
        self.event.set()
        sys.exit(0)

    def run(self):
        """
        run starts all of the mode loops,
        then it starts the mode manager loop and blocks
        until the upstream tries to join
        """

        signal.signal(signal.SIGINT, self.signal_handler)
        pool = Pool(processes=len(self.modes) + len(self.renderers) + 1)
        producerQ = Queue(maxsize=-1)
        consumerQ = Queue(maxsize=-1)
        # Start the producers
        for mode in self.modes:
            pool.apply_async(mode.run, (self.event, producerQ))
        # Start the consumers
        for renderer in self.renderers:
            pool.apply_async(renderer.run, (self.event, consumerQ))
        # Start the producer/consumer broker
        while not self.event.wait(0):
            nextval = producerQ.get(True)
            mode = nextval['name']
            value = nextval['value']
            if mode == self.currentMode:
                consumerQ.put(value)
        pool.close()
        pool.join()

