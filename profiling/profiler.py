import sched
import time
import yappi

import signal
import sys


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    yappi.get_func_stats().print_all()
    yappi.get_thread_stats().print_all()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')

s = sched.scheduler(time.time, time.sleep)

def ping_event(arg):
    print(str(arg))
    arg += 1
    s.enter(1, 1, ping_event, (arg,))

yappi.start()

s.enter(1, 1, ping_event, (1,))

s.run()
