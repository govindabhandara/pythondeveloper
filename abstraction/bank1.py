from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Account class
class Account(ABC):
    def __init__(self, account_number, customer_name, balance=0):
        self._account_number = account_number  # protected attribute
        self._customer_name = customer_name
        self._balance = balance
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(Transaction("Deposit", amount))
            return True
        return False

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    def get_transactions(self):
        return self._transactions

    def __str__(self):
        return f"Account Number: {self._account_number}\nCustomer Name: {self._customer_name}\nBalance: {self._balance}"

# Concrete SavingsAccount class
class SavingsAccount(Account):
    INTEREST_RATE = 0.05  # 5% annual interest

    def withdraw(self, amount):
        if amount > 0 and (self._balance - amount) >= 0:
            self._balance -= amount
            self._transactions.append(Transaction("Withdrawal", amount))
            return True
        return False

    def calculate_interest(self):
        interest = self._balance * self.INTEREST_RATE
        self._balance += interest
        self._transactions.append(Transaction("Interest", interest))
        return interest

# Concrete CurrentAccount class
class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000  # $1000 overdraft allowed

    def withdraw(self, amount):
        if amount > 0 and (self._balance - amount) >= -self.OVERDRAFT_LIMIT:
            self._balance -= amount
            self._transactions.append(Transaction("Withdrawal", amount))
            return True
        return False

    def calculate_interest(self):
        # Current accounts typically don't earn interest
        return 0

# Transaction class to record transactions
class Transaction:
    def __init__(self, transaction_type, amount):
        self.type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.type}: ${self.amount:.2f}"

# Abstract Bank class
class Bank(ABC):
    @abstractmethod
    def create_account(self, account_type, customer_name, initial_deposit):
        pass

    @abstractmethod
    def get_account(self, account_number):
        pass

# Concrete BankImplementation class
class BankImplementation(Bank):
    def __init__(self):
        self._accounts = {}
        self._next_account_number = 1000  # Starting account number

    def create_account(self, account_type, customer_name, initial_deposit):
        account_number = self._generate_account_number()
        
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, customer_name, initial_deposit)
        elif account_type.lower() == "current":
            account = CurrentAccount(account_number, customer_name, initial_deposit)
        else:
            raise ValueError("Invalid account type")
        
        self._accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        return self._accounts.get(account_number)

    def _generate_account_number(self):
        self._next_account_number += 1
        return self._next_account_number

# Example usage
if __name__ == "__main__":
    bank = BankImplementation()
    
    # Create accounts
    alice_savings = bank.create_account("savings", "Govinda", 1000)
    bob_current = bank.create_account("current", "Bob", 500)
    
    # Perform transactions
    alice_account = bank.get_account(alice_savings)
    alice_account.deposit(500)
    alice_account.withdraw(200)
    alice_account.calculate_interest()
    
    bob_account = bank.get_account(bob_current)
    bob_account.withdraw(600)  # This will work due to overdraft
    bob_account.deposit(300)
    
    # Print account information
    print("\nGovinda's Savings Account:")
    print(alice_account)
    print("\nTransactions:")
    for transaction in alice_account.get_transactions():
        print(transaction)
    
    print("\nBob's Current Account:")
    print(bob_account)
    print("\nTransactions:")
    for transaction in bob_account.get_transactions():
        print(transaction)