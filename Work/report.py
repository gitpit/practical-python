'''
https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/02_Containers.html
https://gto76.github.io/python-cheatsheet/#dictionary
# report.py


# Exercise 2.4 A list of tuples
define a function read_portfolio(filename) that opens a given portfolio file and reads it 
into a list of tuples.
'''
def read_portfolio_2_4(fname):
    '''
    # Exercise 2.4 A list of tuples
    return tuples
    '''
    dataTup =()
    dataList = []
    try:        
        with open(fname, 'rt') as f:
            hdr = f.readline()  #ignore hdr
            for line in f:
                #print (line)
                dataTup = line.split(',')
                if len(dataTup) > 2:                    
                    dataList.append(tuple([dataTup[0], int(dataTup[1]), float(dataTup[2])]))
    except FileExistsError:
        print('fiile not found')
    return dataList

## Exercise 2.5: List of Dictionaries
## reading portfolio.csv 
def read_portfolio_2_5(fname):
    '''
    ## Exercise 2.5: List of Dictionaries
    return list
    '''
    dataTup =()
    dataList = []
    try:        
        with open(fname, 'rt') as f:
            hdr = f.readline()  #ignore hdr
            temp = hdr.split(',')            
            for line in f:
                #print (line)
                dataTup = line.split(',')
                if len(dataTup) > 2:
                    #dataList.append(dataTup[0], int(dataTup[1]), float(dataTup[2]))                    
                    dataList.append(dict({'name':dataTup[0], 'shares':dataTup[1], 'price':dataTup[2]}))                                        
    except FileExistsError:
        print('fiile not found')
    return dataList

## Exercise 4.4: reading portfolio.csv  and ret stock objects
import sys
excdir = os.getcwd()
excdir += r'\work'
sys.path
sys.path.append(excdir)

import stock
def read_portfolio_4_4_x(fname):
    '''
    ## Exercise 4.4: reading portfolio.csv  and ret stock objects
    return stock object
    '''    
    stockList = []
    try:        
        with open(fname, 'rt') as f:
            hdr = f.readline()  #ignore hdr
            temp = hdr.split(',')            
            for line in f:
                #print (line)
                dataTup = line.split(',')
                if len(dataTup) > 2:                                                    
                    st = stock.Stock(dataTup[0], int(dataTup[1]), float(dataTup[2]))
                    stockList.append(st)
    except FileExistsError:
        print('fiile not found')
    return stockList

def read_portfolio_4_4(fname):
    '''
    ## Exercise 4.4: reading portfolio.csv  and ret stock objects
    return stock object - using for loop enumerator
    '''    
    try:        
        with open(fname, 'rt') as f:
            hdr = f.readline()  #ignore hdr
            sl = [stock.Stock(s.split(',')[0], int(s.split(',')[1]), float(s.split(',')[2])) for s in f]            
    except FileExistsError:
        print('fiile not found')
    return sl


## calling  above methods
import os
import csv

workDir = os.getcwd()
portFile = workDir + r'\work\data\portfolio.csv'
priceFile =workDir + r'\work\data\prices.csv'
mylist1 = read_portfolio_2_4(portFile)
mylist2 = read_portfolio_2_5(portFile)
mystocks = read_portfolio_4_4_x(portFile)
mystocks = read_portfolio_4_4(portFile)
print(mylist1)
print("-------------------------------")
print(mylist2)
print("-------------------------------")
for ms in mystocks:    
    print(ms.name,ms.shares,ms.price)

## try ...
tDict = {}
i =0
for k in mylist2:   # read each dict from the list
    k.keys()
    k.values()
    k.items()
    k.get('name') 
    xd = dict(zip(k.keys(),k.values()))
    tDict[i] = xd
    i +=1

print(tDict)

## Exercise 2.6: Dictionaries as a container
## Write a function read_prices(filename) that reads a set of prices such as this into a 
## dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.

def read_prices_2_6(fname):
    '''
    ## Exercise 2.6: Dictionaries as a container
    return  dictionary
    '''
    import csv
    dict1 ={}
    try:
        with open(fname,'rt') as f:
            rows = csv.reader(f)
            #hdr = next(rows)
            #print(hdr)
            for row in rows:
                #print(row)
                if(len(row) >= 2):
                    dict1[row[0]] = float(row[1])
    except FileNotFoundError:
        print('File not found -- {}',fname)
    return dict1

dt = read_prices_2_6(priceFile)
print(dt)

'''
##Exercise 2.7: Finding out if you can retire
Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss.
These statements should take the list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute 
the current value of the portfolio along with the gain/loss.
'''
def make_report_data(portfolioFile,pricesFile):
    '''
    ##Exercise 2.7: Finding out if you can retire
    return list: gain_loss
    '''
    pol = read_portfolio_2_4(portfolioFile)
    prd = read_prices_2_6(pricesFile)
    gain_loss = []
    for tu in pol:      # for each tuple in the list        
        strx = str(tu[0]).replace("\"","")
        if strx in prd.keys():
            val = prd.get(strx)
            pur_price = int(tu[1]) * float(tu[2])
            cur_price = int(tu[1]) * float(val)
            if pur_price < cur_price:
                st = 'gain'
            else:        
                st = 'loss'
            val = cur_price - pur_price
            tux = (tu[0],tu[1],tu[2], val,st)            
            gain_loss.append(tux)
    # total loss/gain print
    tot =0
    for a in gain_loss:
        tot = tot + float(a[3])
        print(a)
    print(f'Total loss/gain = {tot:0.4f}')    



## Excercise 4.4 gain_loss using stocks class
def make_report_data_4_4(portfolioFile,pricesFile):
    '''
    ## Excercise 4.4 gain_loss using stocks class
    return list: gain_loss
    '''
    pol = read_portfolio_4_4(portfolioFile) # gets stocks objects
    prd = read_prices_2_6(pricesFile)
    gain_loss = []
    for st in pol:
        strx = str(st.name).replace("\"","")
        if strx in prd.keys():
            cur_price = prd.get(strx)
            pur_cost = st.shares*st.price #  int(tu[1]) * float(tu[2])
            cur_cost = st.shares* float(cur_price)
            if pur_cost < cur_cost:
                status = 'gain'
            else:        
                status = 'loss'
            cost_diff = cur_cost - pur_cost
            tux = (strx,st.shares,st.price, cur_price,cost_diff, status)            
            gain_loss.append(tux)
    # total loss/gain print
    tot =0
    for a in gain_loss:
        tot = tot + float(a[4])
        print(a)
    print(f'Total loss/gain = {tot:0.4f}')    

make_report_data_4_4(portFile,priceFile)   ## using stocks class

make_report_data(portFile,priceFile)


## Exercise 2.8: How to format numbers
##Exercise 2.11: Adding some headers
## Exercise 2.12: Formatting Challenge
def print_report_2_12(port_list, prices_dict):
    '''
    ## print formatted report
    ## Exercise 2.8: How to format numbers
    ##Exercise 2.11: Adding some headers
    ## Exercise 2.12: Formatting Challenge
    '''
    port_status = []
    for tu in port_list:    # for each tuple as row
        strx = str(tu[0].replace("\"",""))
        if strx in prices_dict.keys():
            val = prices_dict.get(strx)
            purchase_price = int(tu[1]* float(tu[2]))
            market_price = int(tu[1]* float(val))
            val = market_price - purchase_price
            tux = (tu[0],tu[1],tu[2], val)   
            port_status.append(tux)
            #port_status.append(tuple(tu[0],tu[1],tu[1],val))
    ## print this in a formatted order
    hdr = ('Name' ,    'Shares'  ,    'Price',     'Change')
    hdr2 = f'{hdr[0]:>10s}{hdr[1]:>10s}{hdr[2]:>10s}{hdr[3]:>10s}'
    #print(f'Name     Shares      Price     Change')
    print(hdr2)
    print(('-'*10 + ' ')*len(hdr))

    for x in port_status:
        print('%10s %10d $%10.2f %10.2f' %(x))

    '''for name,share,price,change in port_status:
        print(f'{name:10s} {share:10d}, {price:$>.2f}, {change:>10.2f}')
        '''
    return port_status

#### 
import tableformat
def print_report_4_5(reportdata, formatter):
    '''
    '''
    formatter.headings(['Name','Shares''Price','Change'])
    for name, shares,price,change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}',f'{change:.2f}']
        formatter.row(rowdata)


def portfolio_report_2(portFile, priceFile):
    '''
    chap2-Make a stock report given portfolio and price data files.
    '''
    pol = read_portfolio_2_4(portFile)
    prd = read_prices_2_6(priceFile)
    print_report_2_12(pol,prd)

def portfolio_report_4_5(portFile,priceFile):
    '''
    chap4-Make a stock report given portfolio and price data files.
    '''
    pol = read_portfolio_4_4(portFile)
    prd = read_prices_2_6(priceFile)
    report = print_report_4_5(pol,prd)
    formatter = tableformat.TableFormatter()
    print_report_4_5(report,formatter)

portfolio_report_2(portFile,priceFile)
portfolio_report_4_5(portFile,priceFile)





