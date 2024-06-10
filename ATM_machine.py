+---------------------+
|        ATM          |
+---------------------+
| - currentAccount: Account |
+---------------------+
| + authenticateUser(cardNumber: String, pin: String): boolean |
| + checkBalance(): double                                     |
| + withdraw(amount: double): void                             |
| + deposit(amount: double): void                              |
| + changePin(newPin: String): void                            |
| + exit(): void                                               |
+---------------------+

           |
           | has a
           |
           v
+---------------------+
|      Account        |
+---------------------+
| - accountNumber: String  |
| - pin: String            |
| - balance: double        |
+---------------------+
| + getBalance(): double   |
| + withdraw(amount: double): void |
| + deposit(amount: double): void  |
| + changePin(newPin: String): void|
+---------------------+

+---------------------+
|    Transaction      |
+---------------------+
| - transactionId: int    |
| - timestamp: String     |
| - amount: double        |
| - type: String          |
+---------------------+
| + Transaction(transactionId: int, timestamp: String, amount: double, type: String) |
| + getTransactionId(): int |
| + getTimestamp(): String  |
| + getAmount(): double     |
| + getType(): String       |
+---------------------+

+---------------------+
|       Bank          |
+---------------------+
| + authenticateUser(cardNumber: String, pin: String): boolean |
+---------------------+


# Account.py
class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def change_pin(self, new_pin):
        self.pin = new_pin

# ATM.py
class ATM:
    def __init__(self):
        self.current_account = None

    def authenticate_user(self, card_number, pin):
        # Logic to authenticate the user against the bank's database
        # For simplicity, let's assume the authentication is successful
        self.current_account = Account("123456789", "1234", 1000.0)  # Dummy account for testing
        return True

    def check_balance(self):
        return self.current_account.get_balance()

    def withdraw(self, amount):
        self.current_account.withdraw(amount)

    def deposit(self, amount):
        self.current_account.deposit(amount)

    def change_pin(self, new_pin):
        self.current_account.change_pin(new_pin)

    def exit(self):
        # Logic to end the ATM session
        pass

# Transaction.py
class Transaction:
    def __init__(self, transaction_id, timestamp, amount, type):
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        self.amount = amount
        self.type = type

# Bank.py
class Bank:
    def authenticate_user(self, card_number, pin):
        # Logic to authenticate the user against the bank's database
        return True  # Dummy implementation for testing

# main.py (for testing)
if __name__ == "__main__":
    atm = ATM()
    atm.authenticate_user("123456789", "1234")
    print("Balance:", atm.check_balance())
