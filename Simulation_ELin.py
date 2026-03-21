
from selbsthilfe_prog2.selbsthilfe_prog2.clock_Elin import Clock as C
from selbsthilfe_prog2.selbsthilfe_prog2.subbancAcc_Elin import SavingAccount as Sa
import time as t
from dateutil.relativedelta import relativedelta

class Simulation:

#Ein Objektattribut, welches jedem einzelnen Objekt individuell ein Wert zuweist.
    def __init__(self):
        self.bancacc = 0
        self.clock = C()
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

    def create_Sa(self, start_amount, IBAN):
        self.bancacc = Sa(IBAN)
        self.bancacc.deposit(start_amount)



def main():
    s1 = Simulation()
    s1.create_Sa(400,"123")



if __name__ == "__main__":
    main()

