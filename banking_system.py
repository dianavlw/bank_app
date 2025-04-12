from datetime import datetime

class Transaction:
    def __init__(self, tx_type, amount):
        self.tx_type= tx_type
        self.amount = amount
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _str_(self):
        return F"{self.date} - {self.tx_type.upper()}: ${self.amount:.2f}"

class BankAccount:
    def __init__(self, account_id, owner_name):
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount <=0:
            print("Deposit amount must be positive")
            return 
        self.balance += amount
        self.transactions.append(Transaction("deposit", amount))
        print(f"Deposited ${amount:.2f} sucessfully.")

    

    def withdraw(self, amount):
        pass

    def show_balance(self):
        pass

    def show_transation(self):
        pass
