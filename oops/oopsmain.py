# #Create a class name bank account , with best and required attributes and methods providing the service of deposit, withdraw, checkbalance 

# class BankAccount:
#     def __init__(self, name, account_number, balance):
#         self.name = name 
#         self.account_number = account_number
#         self.balance = balance
    
#     def deposit(self, amounts):
#         self.balance += amounts
#         return self.balance
    
#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance
    
#     def check_balance(self):
#         return self.balance

#     def transfer(self, receiver_account, amount):
#         if amount <= self.balance and amount > 0:
#             self.balance -= amount
#             receiver_account.balance += amount
#             return f"Transferred {amount} to {receiver_account.name}"
#         return "Insufficient balance or invalid amount"


# account1 = BankAccount("Samir", 1100001, 1200000)
# account2 = BankAccount("Ali", 1100002, 50000)

# print(account1.check_balance())
# print(account1.deposit(1000))
# print(account1.withdraw(100000))
# print(account1.transfer(account2, 500))
# print(account2.check_balance())

