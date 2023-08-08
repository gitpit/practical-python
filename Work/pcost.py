# pcost.py
#
# Exercise 1.27
'''
The columns in portfolio.csv correspond to the stock name, number of shares, 
and purchase price of a single stock holding. Write a program called pcost.py 
that opens this file, reads all lines, and calculates how much it cost to purchase 
all of the shares in the portfolio.
'''
import os
fpath = os.getcwd() 
fpath += r'\Work\Data\portfolio.csv'
f = open(fpath,'rt')
total_cost = 0
next(f)
for line in f:
    data_list = line.split(',')
    cost = int(data_list[1]) *float(data_list[2])
    total_cost += cost
f.close()
print(f'total cost of bying the shares is {total_cost}')

'''
## Exercise 1.28: Other kinds of “files”
What if you wanted to read a non-text file such as a gzip-compressed datafile? 
The builtin open() function won’t help you here, but Python has a library module gzip 
that can read gzip compressed files.
'''
import gzip
import os
fpath = os.getcwd()
fpath += r'\work\data\portfolio.csv.gz'
total_cost = 0
with gzip.open(fpath,'rt') as f:
    next(f)
    for line in f:
        data_list = line.split(',')

        cost = int(data_list[1]) *  float(data_list[2])
        total_cost += cost
print("Total cost of buying all shares = {}", total_cost)

## above script into a method

def portfolio_cost(filename):
    total_cost = 0
    with gzip.open(fpath,'rt') as f:
        next(f)
        for line in f:
            data_list = line.split(',')

            cost = int(data_list[1]) *  float(data_list[2])
            total_cost += cost
    return total_cost

import gzip
import os
fpath = os.getcwd()
fpath += r'\work\data\portfolio.csv.gz'
total_cost = 0
tcost = portfolio_cost(fpath)
print('## Total cost for the shares {0:4f}',tcost)