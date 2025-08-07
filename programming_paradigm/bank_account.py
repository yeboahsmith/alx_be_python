
class BankAccount:
  def __init__ (self, account_balance):
    self.account_balance = account_balance
    self.account_balance = 0

def deposit (amount):
  amount += self.account_balance
  return amount

def withdraw (with_amount):
  WithdrawAmount = self.account_balance - with_amount
  if WithdrawAmount < 0:
    return True
  else:
      return False

 def display_balance():
   print(" Your current balance is: " + self.account_balance )


import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()    
    


