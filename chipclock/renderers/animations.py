import time

def breathe(renderfunc, interval=0.2):
    renderfunc(0, 0)
    time.sleep(interval)
    renderfunc(1, 1)
    time.sleep(interval)
    renderfunc(3, 3)
    time.sleep(interval)
    renderfunc(7, 7)
    time.sleep(interval)
    renderfunc(15,15)
    time.sleep(interval)
    renderfunc(7, 7)
    time.sleep(interval)
    renderfunc(3, 3)
    time.sleep(interval)
    renderfunc(1, 1)
    time.sleep(interval)
