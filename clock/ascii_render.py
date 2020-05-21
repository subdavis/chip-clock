import sys

class AsciiRenderer:
    def __init__(self):
        pass

    def render(self, value):
        print(value)

    def run(self, event, queue):
        """
        Drive the 7-segment from the queue of values
        """
        value = None
        while not event.wait(timeout = 0.1):
            try:
                value = queue.get()
            except queue.Empty:
                pass
            if value:
                self.render(value)
        
