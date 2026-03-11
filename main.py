from selbsthilfe_prog2.selbsthilfe_prog2.clock_Elin import Time as T
from selbsthilfe_prog2.selbsthilfe_prog2.subbancAcc_Elin import SavingAccount as Sa
import time as t

class Simulation:

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

        for m in range(months):
            newmoney = balance * interest
            self.bancacc.deposit(newmoney)
            balance = self.bancacc.get_balance()



def main():
    s1 = Simulation("123")
    s1.bancacc.deposit(4000)
    t.sleep(10)
    s1.actual_balance()




if __name__ == "__main__":
    main()