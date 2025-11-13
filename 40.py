"""Program for BankAccount System with Class and Static Methods@AakashNinan IMCA Rollno:02"""
class BankAccount:
    accounts = []

    def __init__(self, name, balance):
        if not BankAccount.validate_balance(balance):
            raise ValueError("Invalid balance")
        self.name = name
        self.balance = balance
        BankAccount.accounts.append(self)

    @classmethod
    def total_accounts(cls):
        return len(cls.accounts)

    @classmethod
    def total_balance(cls):
        return sum(acc.balance for acc in cls.accounts)

    @staticmethod
    def validate_balance(balance):
        return balance >= 0

    def __str__(self):
        return f"{self.name}: {self.balance}"

a1 = BankAccount("Alice", 1000)
a2 = BankAccount("Bob", 2000)

print("Total accounts:", BankAccount.total_accounts())
print("Total balance:", BankAccount.total_balance())
print(a1)
print(a2)
