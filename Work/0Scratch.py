#this is scratch page to be cleaned each time
print ('#this is scratch page to be cleaned each time')

# read an xls file and print columns....

import csv
import os

workdir = os.getcwd()
datadir = workdir + r'\Work\Data'
portFile = datadir+r'\portfolio.csv'
print(portFile)

with open(portFile,'r') as f:
    rows = csv.reader(f)
    hdr = next(rows)
    print(hdr)
    print("------------------------")
    for row in rows:
        print(row)

priceFile = datadir + r'\prices.csv'
g = open(priceFile,'r')

print("========================\n")
for line in g:
    print(line)

