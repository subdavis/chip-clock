from chipclock.display import ModeDisplay
from chipclock.modes.clock import ClockMode
from chipclock.renderers.time import render_ascii, render_chip

seconds_pins = [
  ['LCD-D5', 'LCD-D11'],
  ['LCD-D4', 'LCD-D10'],
  ['LCD-D3', 'LCD-D7'],
  ['LCD-D2', 'LCD-D6'],
]

disp = ModeDisplay()
clockmode = ClockMode(disp)
disp.register_mode('clock', clockmode, [render_ascii, render_chip(seconds_pins)])
clockmode.run()
