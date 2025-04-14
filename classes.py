import random

class BankAccount():
    def __init__(self, owner, balance, has_overdraft = False):
        self.owner = owner
        self.balance = balance
        self.has_overdraft = has_overdraft
        self.account_no = random.randint(111111111, 999999999)

def deposit (self,amount):
        self.balance += amount
        return self.balance

def withdraw(self,amount):
        if amount > self.balance and self.has_overdraft == False :
            return "Withdrawal denied.No Enough Money"
        else:
            self.balance -= amount
            return self.balance
        
def __str__(self):
        return f"{self.account_no} - Balance{self.balance}"

class SavingAccount(BankAccount):
     def withdraw(self):
        return "No withdrawals permitted"
     
account1 = BankAccount("Ahmed", 300)
print(account1)
print(account1.deposit(200))

print(account1.withdraw(100))
print(account1.withdraw(500))
print (account1)

account2 = BankAccount("Jassim",400, True)
print(account2)
print(account2.withdraw(450))
print(account2.deposit (200))
print(account2)


savings = SavingAccount("Mohamed",700)
print(savings.withdraw())
print(savings)