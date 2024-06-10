
'''

+----------------+
|     Item       |
+----------------+
| - name: String |
| - price: double|
| - quantity: int|
+----------------+
| + getTotalPrice(): double |
+----------------+

+----------------+
|     Cart       |
+----------------+
| - items: List<Item> |
+----------------+
| + addItem(item: Item): void |
| + removeItem(item: Item): void |
| + calculateTotalPrice(): double |
| + applyDiscount(discount: double): void |
| + getItems(): List<Item> |
+----------------+

+----------------+
|     User       |
+----------------+
| - name: String |
| - cart: Cart   |
+----------------+
| + getCart(): Cart |
+----------------+

+----------------------+
|      Payment (interface) |
+----------------------+
| + pay(amount: double): void |
+----------------------+

+-------------------------+
|  CreditCardPayment      |
+-------------------------+
| - cardNumber: String    |
+-------------------------+
| + pay(amount: double): void |
+-------------------------+

+--------------------+
|   PayPalPayment    |
+--------------------+
| - email: String    |
+--------------------+
| + pay(amount: double): void |
+--------------------+



'''

from abc import ABC, abstractmethod

# Item Class
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

# Cart Class
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total_price(self):
        return sum(item.get_total_price() for item in self.items)

    def apply_discount(self, discount):
        total = self.calculate_total_price()
        total -= discount
        return total

# User Class
class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

# Payment Abstract Base Class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# CreditCardPayment Class
class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card ending with {self.card_number[-4:]}")

# PayPalPayment Class
class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount} using PayPal with email {self.email}")

# Main Function to Test the Shopping Cart
def main():
    user = User("John Doe")
    cart = user.cart

    item1 = Item("Laptop", 1000.00, 1)
    item2 = Item("Smartphone", 500.00, 2)

    cart.add_item(item1)
    cart.add_item(item2)

    print("Total Price:", cart.calculate_total_price())

    payment = CreditCardPayment("1234567890123456")
    payment.pay(cart.calculate_total_price())

if __name__ == "__main__":
    main()
