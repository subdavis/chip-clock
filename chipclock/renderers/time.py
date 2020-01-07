import datetime
import time
import sys

from chipclock.renderers.segment import render_segment

def render_ascii(value):
    formatted = time.ctime(value)
    dots = segment(value)
    sys.stdout.write(f'{str(dots)}\r')
    sys.stdout.flush()
    return False # return whether or not it's animating

def render_chip(pins):
    def render(value):
        segments = segment(value)
        seconds = segments[2]
        render_segment(seconds[0], seconds[1], pins)
    return render

def as_binary_digits(number):
    """
    break a number into 2 binary digits
    """
    n = round(number)
    upper = n // 10
    lower = n % 10
    return (upper, lower)

def segment(value):
    dt = datetime.datetime.fromtimestamp(value)
    return [as_binary_digits(dt.hour), as_binary_digits(dt.minute), as_binary_digits(dt.second)]
