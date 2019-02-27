# Class to represent Bill object
# Meant to contain valuable information for any bill
# Most important of these are the due dates and total price

from datetime import date

class Bill:
    
    def __init__(self,name,due_date,price,paid):
        self.name = name
        self.due_date = due_date
        self.price = price
        self.paid = paid

    def update_due(new_due):
        self.due_date = new_due

    def update_price(price):
        self.price = price

    def updatse_paid(paid):
        self.paid = paid

