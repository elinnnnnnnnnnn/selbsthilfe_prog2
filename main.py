<<<<<<< HEAD
# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
from selbsthilfe_prog2.selbsthilfe_prog2.clock_Elin import Time as T
from selbsthilfe_prog2.selbsthilfe_prog2.subbancAcc_Elin import SavingAccount as Sa
import time as t
import datetime
from dateutil.relativedelta import relativedelta

class Simulation:

#Ein Objektattribut, welches jedem einzelnen Objekt individuell ein Wert zuweist.
    def __init__(self,IBAN):
        self.bancacc = Sa(IBAN)
        self.clock = T()
        self.delta = 0
        self.startdate = 0


    def get_passed_time(self):
        self.delta = self.clock.get_delta()
        months = round(self.clock.calc_months(), 0)
        return int(months)

    def actual_balance(self):
        months = self.get_passed_time()
        interest = self.bancacc.get_interest()
        balance = self.bancacc.get_balance()
        date = self.clock.get_date()

        for m in range(months):
            date += relativedelta(months=1)
            print(f"Sie haben am {date.strftime('%Y-%m-%d')} den Zins erhöht")
            newmoney = balance * interest
            self.bancacc.deposit(newmoney)
            balance = self.bancacc.get_balance()



def main():
    s1 = Simulation("123")
    s1.bancacc.deposit(4000)
    t.sleep(25)
    s1.actual_balance()



if __name__ == "__main__":
    main()
>>>>>>> 5bde5e13c87555aa6ad55c06e9cc7edeb47d42d4
