# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time
def job_scheduler(f, n):
    while True:
        f('hi')
        time.sleep(n)
ff_ = lambda b: print(b)
job_scheduler(ff_, 5)

# another way 
import threading
def delay(delay=0.):
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args, kwargs)
            timer.start()
        return delayed
    return wrap




