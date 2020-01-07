import CHIP_IO.GPIO as GPIO

def setup_pins(pins_list):
    for pins in pins_list:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)

def render_segment(left, right, pins, bits=4):
    """
    left: nibble
    right: nibble
    pins:
    [
        [8, 8]
        [4, 4]
        [2, 2]
        [1, 1]
    ]
    """
    orders = range(bits - 1, -1, -1)
    for bit, pin in zip(orders, pins):
        leftval = (left >> bit) & 1
        rightval = (right >> bit) & 1
        GPIO.output(pin[0], left)
        GPIO.output(pin[1], right)
