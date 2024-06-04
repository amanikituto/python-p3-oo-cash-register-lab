#!/usr/bin/env python3
import unittest
from lib.CashRegister import CashRegister

class TestCashRegister(unittest.TestCase):

    def test_initial_total(self):
        register = CashRegister()
        self.assertEqual(register.total, 0)

    def test_add_item(self):
        register = CashRegister()
        register.add_item("apple", 1.00)
        self.assertEqual(register.total, 1.00)
        self.assertEqual(register.items, ["apple"])

    def test_apply_discount(self):
        register = CashRegister(discount=20)
        register.add_item("banana", 1.00)
        register.apply_discount()
        self.assertEqual(register.total, 0.80)

    def test_void_last_transaction(self):
        register = CashRegister()
        register.add_item("orange", 1.00)
        register.void_last_transaction()
        self.assertEqual(register.total, 0)

if __name__ == "__main__":
    unittest.main()
class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.discount = discount
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.items.extend([price]*quantity)
        self.last_transaction = price * quantity

    def total(self):
        return float(sum(self.items))

    def apply_discount(self):
        if self.discount:
            new_total = self.total() * (1 - (self.discount / 100))
            return f"After the discount, the total comes to ${new_total:.2f}"
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        for _ in range(int(self.last_transaction)):
            self.items.pop()