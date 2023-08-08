# pcost.py
#
# Exercise 1.27
'''
The columns in portfolio.csv correspond to the stock name, number of shares, 
and purchase price of a single stock holding. Write a program called pcost.py 
that opens this file, reads all lines, and calculates how much it cost to purchase 
all of the shares in the portfolio.
'''
## above script into a method
import gzip
import os
def portfolio_cost(filename):
    total_cost = 0
    with gzip.open(fpath,'rt') as f:
        next(f)
        for line in f:
            data_list = line.split(',')

            cost = int(data_list[1]) *  float(data_list[2])
            total_cost += cost
    return total_cost


fpath = os.getcwd()
fpath += r'\work\data\portfolio.csv.gz'
total_cost = 0
tcost = portfolio_cost(fpath)
print('## Total cost for the shares {0:4f}',tcost)

