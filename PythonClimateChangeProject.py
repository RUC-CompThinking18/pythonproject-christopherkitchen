"""import datetime
import time
today = date.today()
the_end = date(2030, 1, 1)"""

"""import time
boom = int(input("Countdown form:"))
while boom > 0:
    time.sleep(1)
    print(boom)
    boom -= 1
print("u died")"""

import time
import sys

def run_timer(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write("\r")
        minutes = 0
        seconds = remaining
        if remaining > 60:
            minutes = int(seconds/60)
            seconds = int(seconds%60)
        else:
            seconds = remaining
        sys.stdout.write("{:2d} minutes {:2d} seconds remaining.".format(minutes,seconds))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(" you died")

run_timer(120)
