from chipclock.display import ModeDisplay
from chipclock.modes.clock import ClockMode
from chipclock.renderers.time import render_ascii, render_chip
from chipclock.renderers.segment import setup_pins, render_segment

seconds_pins = [
  ['LCD-D5', 'LCD-D11'],
  ['LCD-D4', 'LCD-D10'],
  ['LCD-D3', 'LCD-D7'],
  ['LCD-D20', 'LCD-D6'],
]
setup_pins(seconds_pins)
renderfunc = render_segment(seconds_pins)
disp = ModeDisplay()
clockmode = ClockMode(disp)
disp.register_mode('clock', clockmode, [render_ascii, render_chip(renderfunc)])
clockmode.run()
