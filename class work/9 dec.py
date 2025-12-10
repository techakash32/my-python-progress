import random

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = random.randint(10000000, 99999999)
        self.account_holder = account_holder
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance
    
    def balance_update(self):
        self.__balance -= 1
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Allows child class to modify balance safely
    def _deduct(self, amount):
        self.__balance -= amount

    def _can_withdraw(self, amount):
        return self.__balance >= amount


class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)
        self.minimum_balance = 5000

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return
        
        current_balance = self.get_balance()

        if current_balance - amount >= self.minimum_balance:
            self._deduct(amount)
            print(f"Withdrawn: {amount}")
        else:
            print("Cannot withdraw: Minimum balance of ₹5000 must remain.")


# ----------- Testing -------------
b1 = BankAccount("akash", 1000)

print(b1.get_balance())       
print(b1.balance_update())   
