from subaccounts import SavingAccount
from subaccounts import YouthAccount


class BankApplication:
    pass

    def __init__(self):
        self.current_account = None
        self.current_user = None
        self.accounts = []

    def authenticate(self):
        pass

    def open_account(self):
        choice = input("Choose account type (1=Saving, 2= Youth):")
        if choice == "1":
            identifier = input("Enter account identifier")
            account = SavingAccount(identifier)

        elif choice == "2":
            identifier = input("Enter account identifier")
            age = int(input("Enter Age: "))
            account = YouthAccount(identifier, age)

        self.accounts.append(account)

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
            choice = int(input("Choose an account by his number"))
            index = choice - 1
            self.current_account = self.accounts[index]
            print("Selected account:", self.current_account.identifier)


    def run(self):
        pass


class TaxReport:
    pass



def main():
    #
    #
    #
    #
if __name__ == "__main__":
    main()
    $