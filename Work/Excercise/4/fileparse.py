# fileparse.py
#Reading CSV Files
# Exercise 3.3

import os
import csv

def parse_csv(filename):
    '''
    Parse a csv file ito a list of records
    '''
    records = []
    with open(filename,'rt+') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            rec = dict(zip(headers,row))            
            records.append(rec)
            print(rec)
    return records
workdir = os.getcwd()
workdir += r'\work'


def parse_csv2(filename, select=None):
    records = []
    with open(filename,'rt+') as g:
        rows = csv.reader(g)
        header = next(rows)
        if select:
            indices = [header.index(colname) for colname in select]
            header = select
        else:
            indices = []
        #hdr2 = [header2[0],header2[1]]
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]    #dict(zip(select,row))
            rec = dict(zip(header,row))
            records.append(rec)
    return records

'''' 
method callers
'''
recs = parse_csv(workdir+r'\data\portfolio.csv')
recs2 = parse_csv2(workdir+r'\data\portfolio.csv',['name','shares'])
print()
print("-------------\n")
for r in recs2:
    print(r)

'''
            3.5 Main Module
            Python has no main function or method. Instead, there is a main module. The main module is the source file that runs first.
            __main__ check
            It is standard practice for modules that run as a main script to use this convention:

            Main programs vs. library imports
            Any Python file can either run as main or as a library import:
            
            bash % python3 prog.py # Running as main

            import prog   # Running as library import

'''

'''
 Python Program Template -- order
'''
# prog.py
# Import statements (libraries)
#import modules

# Functions
def spam():
    ...

def blah():
    ...

# Main function
def main():
    ...

'''
if __name__ == '__main__':
    main()
'''