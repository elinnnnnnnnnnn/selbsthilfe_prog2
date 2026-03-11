from selbsthilfe_prog2.selbsthilfe_prog2.bancAcc_Elin import BankAccount


class SavingAccount(BankAccount):
    def __init__(self,identifier, interest = 0.001):
        super().__init__(self)
        self.identifier = identifier
        self.interest = float(interest)
        self.withdrawcost = 0.2


    def set_interestrate(self):
        if self.is_open == True:
            intr = float(input("Set interest in Prozent"))
            self.interest = intr / 100

#Gibt Zinsen für Computer zurück
    def get_interest(self):
        return self.interest

    def print_interest(self):
        return f"Bankacc:{self.identifier} hat {self.interest * 100}% Zinsen"

    def withdraw(self, amount):
        if self.is_open == True:
            if self.balance - amount > 0:
                self.balance -= amount
                print(f"Your actual Balance is: {self.balance}{self.currency}.")

            else:
                namount = (amount + amount * self.withdrawcost)
                self.balance -= namount
                print(f"Your balance is below zero, every withdraw costs additional {self.withdrawcost *100}% -> {namount} ")
        else:
            print("Withdraw now possible. Your account is closed.")

class YouthAccount(BankAccount):
    def __init__(self,identifier, age, interest = 0.02):
        super().__init__(self)
        self.age = age
        if self.age < 0 or self.age > 25:
            raise ValueError("Das Alter ist für diesen Account ungültig")

        self.interest = float(interest)
        self.withmax = 2000


    def set_interestrate(self):
        if self.is_open == True:
            intr = float(input("Set interest in Prozent"))
            self.interest = intr / 100

    def get_interest(self):
        return f"Sie haben {self.interest * 100} % Zinsen"


    def withdraw(self, amount):
        if self.withmax - amount >= 0:
            self.withmax -= amount
            BankAccount.withdraw(self, amount)
        else:
            print(f"Maximales Monatslimit erreicht")




def main():
    b1 = YouthAccount("134",23)
    b1.deposit(15000)
    b1.withdraw(200)
    b1.get_balance()


if __name__ == "__main__":
    main()