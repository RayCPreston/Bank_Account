# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 06:54:49 2020

@author: Ray.Preston
"""

#bank account class
#deposit, withdraw, transfer, getBalance, checkFunds
class Account(object):
    def __init__(self, balance=0):
        self.balance = balance
    def getBalance(self) -> float:
        return self.balance
    def deposit(self, depositAmount):
        self.balance += depositAmount
        print("Your new balance is: " + str(self.balance))
    def checkFunds(self, check) -> bool:
        if self.balance >= check:
            return True
        else:
            return False
    def withdraw(self, withdrawAmount):
        if self.checkFunds(withdrawAmount):
            self.balance -= withdrawAmount
            print("Your new balance is: " + str(self.balance))
        else:
            print("You have no monies for that!")
    def transfer(self, transferAmount, recipient):
        if self.checkFunds(transferAmount):
            self.balance -= transferAmount
            recipient.deposit(transferAmount)
        else:
            print("You have no monies for that!")

account1 = Account(1500)
account2 = Account(1000)
print(account1.getBalance())
account1.deposit(500)
print(account1.getBalance())
account1.withdraw(2001)
account1.withdraw(250)
print(account2.getBalance())
account1.transfer(250, account2)
print(account1.getBalance())
print(account2.getBalance())