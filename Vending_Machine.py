+---------------+           +---------------+
|    Item       |<>-------o|  Inventory    |
+---------------+           +---------------+
| - name        |           | - items: dict |
| - price       |           |               |
| - quantity    |           |               |
+---------------+           +---------------+
      |                            |
      |                            |
      |                            |
+---------------+           +---------------+
|   Coin        |           | Transaction   |
+---------------+           +---------------+
| - value       |           | - total       |
+---------------+           | - paid_amount |
                             +---------------+
                                     |
                                     |
                                     |
                             +---------------+
                             | VendingMachine|
                             +---------------+
                             | - inventory   |
                             | - transaction |
                             +---------------+


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def decrease_quantity(self):
        self.quantity -= 1

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        self.items[name] = Item(name, price, quantity)

    def get_item(self, name):
        return self.items.get(name)

class Coin:
    def __init__(self, value):
        self.value = value

class Transaction:
    def __init__(self):
        self.total = 0
        self.paid_amount = 0

    def add_item(self, item):
        self.total += item.price

    def add_payment(self, amount):
        self.paid_amount += amount

    def get_remaining_amount(self):
        return self.total - self.paid_amount

    def is_fully_paid(self):
        return self.paid_amount >= self.total

class VendingMachine:
    def __init__(self):
        self.inventory = Inventory()
        self.transaction = Transaction()

    def add_item(self, name, price, quantity):
        self.inventory.add_item(name, price, quantity)

    def select_item(self, name):
        item = self.inventory.get_item(name)
        if item:
            self.transaction.add_item(item)
        else:
            print("Item not available.")

    def insert_coin(self, value):
        self.transaction.add_payment(value)

    def process_transaction(self):
        if self.transaction.is_fully_paid():
            print("Transaction successful. Enjoy your item!")
            item = self.transaction.item
            item.decrease_quantity()
        else:
            print("Insufficient funds. Please insert more coins.")
