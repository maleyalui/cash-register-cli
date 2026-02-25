#!/usr/bin/env python3

class CashRegister:

  def __init__(self,discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self,value):
    if isinstance(value, int) and 0 <= value <=100:
      self._discount = value
    else:
      print("Not valid discount")
      self._discount = 0

  def add_item(self,item,price, quantity = 1):
    line_total = price * quantity
    self.total += line_total

    for _ in range(quantity):
      self.items.append(item)


    #Track transactions for potential voiding
    self.previous_transactions.append ( {
      "item": item,
      "price": price,
      "quantity": quantity,
      "line_total": line_total
    })

  def apply_discount(self):
    # If no discount is set
    if self.discount == 0:
        print("There is no discount to apply.")
        return

    multiplier = self.discount / 100
    self.total -= (self.total * multiplier)

    print(f"After the discount, the total comes to ${self.total:g}.")

  def void_last_transaction(self):
      if not self.previous_transactions:
        print("No transactions to void.")
        return

      last_transaction = self.previous_transactions.pop()
      self.total -= last_transaction["line_total"]


      for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])
  
