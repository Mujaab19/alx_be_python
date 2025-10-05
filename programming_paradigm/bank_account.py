# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # private attribute for encapsulation
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            # do not change balance for invalid deposit
            print("Deposit amount must be positive.")
            return
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # user-friendly print of current balance
        print(f"Current Balance: ${self.__account_balance}")
