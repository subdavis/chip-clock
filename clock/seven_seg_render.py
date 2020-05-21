"""
GPIO code to render 7-segment multi-character display
on a C.H.I.P. by NextThing Co.

Seven segment should be wired like this
And the anode pins should be in this order

    0
   ===
5 |   | 1
  |   |
   =6=
4 |   | 2
  |   |
   ===
    3
"""

import datetime
import queue
import time

import CHIP_IO.GPIO as GPIO

from .utils import as_digits

#Numerals
ZERO = 0b00111111
ONE  = 0b00000110
TWO  = 0b01011011
THREE= 0b01001111
FOUR = 0b01100110
FIVE = 0b01101101
SIX  = 0b01111110
SEVEN= 0b00000111
EIGHT= 0b01111111
NINE = 0b01100111

NUMERALS = [
    ZERO,
    ONE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE,
]

class SevenSegRenderer:
    def __init__(self, anode_pins, cathode_pins):
        """
        anode_pins (positive pins)
        cathode_pins (1+ negative pins)
        """
        self.anode_pins = anode_pins
        self.cathode_pins = cathode_pins
        self.value = None
        self.bitsPerChar = len(anode_pins)
        self.digits = len(cathode_pins)

    def writeDigit(self, char):
        # Iterate over bits from [bit_i -> 0]
        orders = range(0, self.bitsPerChar - 1)
        for bit, pin in zip(orders, self.pinlist):
            val = (char >> bit) & 1
            GPIO.output(pin, val)
    
    @staticmethod
    def formatTime(value):
        dt = datetime.datetime.fromtimestamp(value)
        hours = as_digits(dt.hour, 2)
        minutes = as_digits(dt.minute, 2)
        seconds = as_digits(dt.second, 2)
        return [
            NUMERALS[hours[0]],
            NUMERALS[hours[1]],
            NUMERALS[minutes[0]],
            NUMERALS[minutes[1]],
            NUMERALS[seconds[0]],
            NUMERALS[seconds[1]],
        ]

    def writeDigits(self, chars):
        """
        Characters will be written to the 7-segment
        first-to-last on cathode pins, so [NINE, THREE, TWO, ZER0]
        would come out '9 3 2 0' IFF the 9's digit is the
        first cathode pin in the cathode array.
        """
        for i, char in enumerate(chars):
            if len(self.cathode_pins) > i:
                # Set the cathode to SINK
                GPIO.output(self.cathode_pins[i], GPIO.LOW)
                # Write the digit to the annodes
                self.writeDigit(char)
                # Pause
                time.sleep(0.001)
                # Set the cathode to SOURCE
                GPIO.output(self.cathode_pins[i], GPIO.HIGH)
            else:
                pass

    def setup_pins(self):
        for pin in self.cathode_pins:
            GPIO.setup(pin, GPIO.OUT)
        for pin in self.anode_pins:
            GPIO.setup(pin, GPIO.OUT)

    def run(self, event, queue):
        """
        Drive the 7-segment from the queue of values
        """
        self.setup_pins()
        value = None
        while not event.wait(0):
            try:
                value = queue.get(False)
            except queue.Empty:
                pass
            if value:
                char = NUMERALS[round(value) % 10]
                self.draw(char)
