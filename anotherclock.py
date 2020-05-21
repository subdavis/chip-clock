from multiprocessing.dummy import Pool, Queue, Event

from clock.ascii_render import AsciiRenderer
from clock.clock import ClockMode
from clock.clock import DisplayDriver
from clock.seven_seg_render import SevenSegRenderer

cm = ClockMode('clock1', SevenSegRenderer.formatTime)
ar = AsciiRenderer()
dd = DisplayDriver([cm], [ar])
dd.currentMode = 'clock1'
dd.run()
