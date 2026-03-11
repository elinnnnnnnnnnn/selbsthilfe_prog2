import time
from datetime import datetime as dt
import time as t

class Time:
    timeformonth = 10
    def __init__(self):
        self.start = t.time()
        self.delta = 0

    def get_actual_time(self):
        self.current_time = t.time()
        return self.current_time

    def get_delta(self):
        self.delta = t.time() - self.start
        return self.delta

    def calc_months(self):
        months = self.delta / self.timeformonth
        return months




def main():
    t1 = Time()
    print(t1.get_actual_time())
if __name__ == "__main__":
    main()