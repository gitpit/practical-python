#ticker.py
import sys
import os

excdir = os.getcwd()
excdir += r'\work'
sys.path
sys.path.append(excdir)

from follow import follow
import csv
from  report import read_portfolio_6_2



def select_columns(rows, indices):
    for row in rows:
        yield[ row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

''' TODO: -- ticker method
'''
def ticker(portfile, logfile):    
    import report
    portfolio = report.read_portfolio_2_6(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)

ticker('data/portfolio.csv','data/stocklog.csv')

if __name__ == '__main__':
    lines = follow('work\data\stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)

## 6.4 more generators

i