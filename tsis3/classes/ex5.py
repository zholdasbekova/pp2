class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal failed. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")


account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(800)  
