class BankingSystem:
    def __init__(self):
        self.balance=100000
    def deposit(self, amount):
        if (abs(amount)<=self.balance) or (amount>=0):
            print("Current Balance : ",self.balance)
            self.balance+=amount
            print("Updated Balance : ",self.balance,end="\n\n")
        else:
            print("Invalid Transaction....",end="\n\n")
    def withdraw(self, amount):
        self.deposit(-amount)

class AutomatedTellerMachine(BankingSystem):
    pass

User = AutomatedTellerMachine()
User.withdraw(102000)
User.deposit(2000)
User.withdraw(102000)
        
        
        
