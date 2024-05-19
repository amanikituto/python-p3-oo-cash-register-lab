#!/usr/bin/env python3

class CashRegister:
  pass
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.last_transaction = None
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount:
            self.total = self.total - (self.total * (self.discount / 100.0))
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = None