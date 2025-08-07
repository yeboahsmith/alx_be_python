
class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, with_amount):
        if with_amount > self.account_balance:
            print("Insufficient funds.")
            return False
        else:
            self.account_balance -= with_amount
            return True

    def display_balance(self):
        print("Your current balance is: $" + str(self.account_balance))






