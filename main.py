class mpesaaccount:
    def __init__ (self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return (f"{amount} was deposited")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"

        self.balance -= amount
        return print(f"{amount} was withdrawn")

    def check_balance(self):
        return self.balance

account = mpesaaccount("Feddy", 5000)

print(account.deposit(2000))
print(account.check_balance())
                    
print(account.withdraw(3000))
print(account.check_balance())

print(account.withdraw(6000))
print(account.check_balance())
