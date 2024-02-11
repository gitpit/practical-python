'''
Exercise 4.1: Objects as Data Structures
Exercise 4.2: Adding some Methods
'''

class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares* self.price
    def sell(self,quantity):
        self.shares -= quantity
    def buy(self,quantity,price):        
        self.price = (quantity*price + self.shares*self.price)/(quantity+self.shares)
        self.shares +=quantity

# using inheritance
class MyStock (Stock):
    def __init__(self,name,shares,price,factor):
        super().__init__(name,shares,price)
        self.factor = factor
    def cost(self):
        return self.factor* super().cost()
