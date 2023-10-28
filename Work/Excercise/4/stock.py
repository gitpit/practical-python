'''
Exercise 4.1: Objects as Data Structures
Creating stock class
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