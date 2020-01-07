import sys
import time

def restart_line():
    sys.stdout.write('\r\r')
    sys.stdout.flush()

sys.stdout.write('some data\n')
sys.stdout.write('other data')
sys.stdout.flush()
time.sleep(2) # wait 2 seconds...
restart_line()
sys.stdout.write('other different data\n')
sys.stdout.write('asfsfd')
sys.stdout.flush()
