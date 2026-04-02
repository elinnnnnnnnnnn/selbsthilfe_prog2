from datetime import datetime as dt
import time as t

class Clock:
    TIMEFORMONTH = 1
    def __init__(self):
        self.start = t.time()
        self.delta = 0
        self.date = dt.now()

    def get_actual_time(self):
        self.current_time = t.time()
        return self.current_time

    def get_delta(self):
        self.delta = t.time() - self.start
        return self.delta

    def get_date(self):
        date = self.date
        return date

    def calc_months(self):
        months = self.delta / self.TIMEFORMONTH
        return months




def main():
    t1 = Clock()
    print(t1.get_date())

if __name__ == "__main__":
    main()