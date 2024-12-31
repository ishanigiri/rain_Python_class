class BankAccount:
    def __init__(self, name):
        self._balance = 0
        self.name = name
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        self._balance -= amount
    def get_balance(self):
        return self._balance
    def __str__(self):
        return f"Name: {self.name} and Balance: Hidden"
# Example 8: using encapsulation
ishani = BankAccount("ishani")
ishani.deposit(100)
print(ishani)      
print(ishani.get_balance())
ishani.withdraw(50)
ishani.deposit(400)
ishani.withdraw(100)
print(ishani.get_balance())
