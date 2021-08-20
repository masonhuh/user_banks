class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
    
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if (self.balance > amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insuffienct funds: Charging a $5 fee")
            return self

    def display_account_info(self):
        # your code here
        print(f"Balnace: {self.balance}")

    def yield_interest(self):
        # your code here
        if (self.balance > 0):
            self.balance *= (self.int_rate + 1)
        return self

    @classmethod
    def get_all_info(cls):
        for account in cls.accounts:
            print(f"Your interest rate is: {account.int_rate} Your balance is: {account.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance = 0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

class SavingAccount(BankAccount):
    def __init__(self, int_rate, balance=0):
        super().__init__(int_rate, balance)
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.1
        super().withdraw(amount)
        return self

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self