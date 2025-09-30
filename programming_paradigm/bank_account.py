#simulation of a bank to apply the knowledge of Object Oriented Programming(OOP)

class BankAccount:
    def __init__(self, initial_deposit = 0):
        self.account_balance = initial_deposit
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Please deposit some amount to deposit.")
        
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False
            
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")


        