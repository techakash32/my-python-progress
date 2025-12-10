class bankaccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

b1 = bankaccount("123456789", "John Doe", 1000)
b1.deposit(500)
print(b1.balance)  # Output: 1500
b1.deposit(-200)  # Output: Deposit amount must be positive.
b1.withdraw(300)
print(b1.balance)  # Output: 1200

