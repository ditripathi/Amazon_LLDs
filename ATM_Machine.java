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




// Account.java
public class Account {
    private String accountNumber;
    private String pin;
    private double balance;

    public Account(String accountNumber, String pin, double balance) {
        this.accountNumber = accountNumber;
        this.pin = pin;
        this.balance = balance;
    }

    public double getBalance() {
        return balance;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void changePin(String newPin) {
        pin = newPin;
    }
}

// ATM.java
public class ATM {
    private Account currentAccount;

    public boolean authenticateUser(String cardNumber, String pin) {
        // Logic to authenticate the user against the bank's database
        // For simplicity, let's assume the authentication is successful
        currentAccount = new Account("123456789", "1234", 1000.0); // Dummy account for testing
        return true;
    }

    public double checkBalance() {
        return currentAccount.getBalance();
    }

    public void withdraw(double amount) {
        currentAccount.withdraw(amount);
    }

    public void deposit(double amount) {
        currentAccount.deposit(amount);
    }

    public void changePin(String newPin) {
        currentAccount.changePin(newPin);
    }

    public void exit() {
        // Logic to end the ATM session
    }
}

// Transaction.java
public class Transaction {
    private int transactionId;
    private String timestamp;
    private double amount;
    private String type;

    // Constructor, getters, and setters
}

// Bank.java
public class Bank {
    public boolean authenticateUser(String cardNumber, String pin) {
        // Logic to authenticate the user against the bank's database
        return true; // Dummy implementation for testing
    }
}

// Main.java (for testing)
public class Main {
    public static void main(String[] args) {
        ATM atm = new ATM();
        atm.authenticateUser("123456789", "1234");
        System.out.println("Balance: " + atm.checkBalance());
    }
}
