from subaccounts import SavingAccount
from subaccounts import YouthAccount


class BankApplication:
    pass

    def __init__(self):
        self.current_account = None
        self.current_user = None
        self.accounts = []

    def authenticate(self):
        user = input("Please enter your username: ")
        self.current_user = user

    def open_account(self):

        choice = input("Choose account type (1=Saving, 2= Youth): ")

        if choice == "1":
            identifier = input("Enter account identifier: ")
            account = SavingAccount(identifier)
            self.accounts.append(account)


        elif choice == "2":
            identifier = input("Enter account identifier: ")
            try:
                age = int(input("Enter Age: "))
            except ValueError:
                print("Invalid age. Please enter e valid one.")
                return

            account = YouthAccount(identifier, age)
            self.accounts.append(account)


        else:
            print("Invalid input. Please choose between 1 or 2: ")

    def show_accounts(self):
        if not self.accounts:
            print("No accounts available")
        else:
            for i, a in enumerate(self.accounts):
                print(i + 1, "-", a.identifier)


    def close_account(self):
        if self.current_account is None:
            print("No active account at the moment.")
        else:
            self.current_account.deactivate()
            print(f"Account {self.current_account.identifier} closed.")

    def select_account(self):
        if not self.accounts:
            print("No accounts available")
        else:
            self.show_accounts()
            try:
                choice = int(input("Choose an account by his number: "))
                index = choice - 1
                self.current_account = self.accounts[index]
                print("Selected account:", self.current_account.identifier)
            except ValueError:
                "Invalid choise. Please try again."
                return

    def run(self):
        while True:
            print("Menue:")
            print("1-Open Account")
            print("2-Show Account")
            print("3-Select Account")
            print("4-Close Account")
            print("5-Exit")
            try:
                choice = int(input("Please choose an option: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.open_account()
            elif choice == 2:
                self.show_accounts()
            elif choice == 3:
                self.select_account()
            elif choice == 4:
                self.close_account()
            elif choice == 5:
                break


class TaxReport:                    # Kein Konstruktor nötig. Nur wenn eigene Daten gespeichert werden müssen
    def generate(self, bank_app):
        savings_total = 0
        youth_total = 0

        for account in bank_app.accounts:
            if isinstance(account, SavingAccount):
                savings_total += account.balance
            elif isinstance(account, YouthAccount):
                youth_total += account.balance

        print("Tax report")
        print(f"** Savings Account ** {savings_total:.2f} Fr")
        print(f"** Youth Account ** {youth_total:.2f} Fr")


def main():
    app = BankApplication()
    app.authenticate()
    app.run()


if __name__ == "__main__":
    main()
