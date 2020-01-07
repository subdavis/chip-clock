import math
import time
import sched

class ClockMode:

    def __init__(self, display):
        self.display = display
        self.value = None
        self.active = True

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True
    
    def update_value(self):
        self.value = time.time()
        self.display.notify()

    def run(self):
        self.update_value()
        s = sched.scheduler(time.time, time.sleep)
        while self.active:
            t =  math.floor(time.time()) + 1
            s.enterabs(t, 1, self.update_value)
            s.run()
