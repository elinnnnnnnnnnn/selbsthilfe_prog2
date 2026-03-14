
class BankAccount:

    MAX = 100_000
    def __init__(self, identifier):
        self.identifier = identifier
        self.__balance = 0.0
        self.currency = "CHF"
        self.is_open = True

    def set_status(self):
        pass
    def status(self):
        if self.is_open:
            return f"The Bank Account {self.identifier} is open."
        else:
            return f"The Bank Account {self.identifier} is closed. No Action possible."

    def deposit(self, amount):
        if self.is_open:
            if self.__balance + amount > self.MAX:
                print("Deposit not possible. Limit of 100000 exceeded.")
            else:
                self.__balance += amount
                print(f"Einzahlung von {amount} {self.currency} ")
                print(f"Your actual Balance is: {self.__balance}{self.currency}.")
                print(f"+---------------IBAN:{self.identifier}----------------+")
        else:
            print(f"Your account is closed.")


    def withdraw(self, amount):
        if self.is_open:
            if self.__balance - amount > 0:
                self.__balance -= amount
                print(f"Your actual Balance is: {self.__balance}{self.currency}.")

            else:
                print("Withdraw not possible. Balance would be below zero.")
        else:
            print("Withdraw not possible. Your account is closed.")


    def get_balance(self):
        if self.is_open == True:
            return self.__balance


def main():
    ba1 = BankAccount("CH123")

    print(ba1.status())
    print(ba1.get_balance())

    ba1.deposit(10000000)
    ba1.status()


if __name__ == "__main__":
    main()



