#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):  # Add default discount value
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.discount = discount
        self.last_transaction = 0.0 
        

    def add_item(self, item_name, price, quantity=1):  # Make quantity optional
        for _ in range(quantity):
            self.items.append((item_name))
        self.total += price * quantity  # Update total accordingly
        self.last_transaction = price * quantity  # Update last transaction

    def apply_discount(self):
      if self.discount > 0:
        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount
        formatted_total = f"${int(self.total)}" if self.total.is_integer() else f"${self.total:.2f}"
        print(f"After the discount, the total comes to {formatted_total}.")
      else:
        print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction  # Subtract last added item's price
        self.last_transaction = 0  # Reset last transaction    
