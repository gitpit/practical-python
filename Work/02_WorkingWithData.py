'''
# Chap 2: Working with Data
https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/00_Overview.html
2.1 Datatypes and Data Structures
2.2 Containers
2.3 Formatted Output
2.4 Sequences
2.5 Collections module
2.6 List comprehensions
2.7 Object model

'''
        ##### 2.1 Datatypes and Data structures
        #####

## none type: None is often used as a placeholder for optional or missing value. It evaluates as False in conditionals.
email_addr = None

    ## Tuples   ()- collection of values grouped together. represent simple records or structures.
    ## A good analogy: A tuple is like a single row in a database table.
    ## Contents are ordered but can not be modified. It is read only

s = ('GOOG', 100,440.23)
s1 = 'YAHO',88,212.12   # is also tuple type and bracket is optional
s2 = ()     # an empty tuple
print(s[2])

    # Tuple packing -- like swift programming lang; related items are packed together in a single entity.
    # this is then passed to function or returned from function.
s = ('Id',22,'F')   # id, age and gender can be packed together
print(s)

# Tuple unpacking -- tuple elements can be unpacked to use it elsewhere
id,age,gender = s   
print(id,age,gender)

    ## Dictionaries { } -- key value mapping
    ##
s = { 'id':'Id11',
      'age':22,
      'Gender': 'F'
    }

print(s['id'])

# excercise using tuple, reading csv file
import os
import csv

fpath = os.getcwd()
fpath += r'\work\data\portfolio.csv'
with open(fpath,'rt') as f:
    rows =csv.reader(f)
    hdr =next(rows)
    print(hdr)
    r = next(rows)
    print(r)
    (a,b,c)  = next(rows)
    print(a,b,c)
    for row in rows:
        (a,b,c) = row
        print((a,b,c))        
        print("---" + row[0],row[1])

# iterate throught dict items
dict1 = s
items = dict1.items()
print(items)
for i in dict1:
    print(i, dict1[i])


'''
######  2.2 Containers
==============
Lists. Ordered data.
Dictionaries. Unordered data.
Sets. Unordered collection of unique items.
'''
# list of tuples
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]
# list of dictionaries
portfolio2 = [
    {'name': 'GOOG', 'shares' :100, 'price':490.1},
    {'name': 'IBM', 'shares' :50, 'price':90.1},
    {'name': 'CAT', 'shares' :150, 'price':49.1},    
]
x1 = []
x1.append("one")
len(x1)
print(x1)
#dict

priceList = []  # list 
priceDict = {}  #dict
def prices_ex():
    import os
    import csv
    fpath = os.getcwd()
    fpath += r'\work\data\prices.csv'
    with open(fpath,'rt') as f:        
        for line in f:
            xm = line.split(',')
            if len(xm) >=2:            
                priceList.append([xm[0],float(xm[1])])                
                priceDict[xm[0]] = float(xm[1])        
    print(priceList)
    print(priceDict)    
prices_ex()
for d in priceDict:
    print(d,priceDict.get(d))

print(priceDict.get('IBM',0.0))

## Sets  {} -Sets are collection of unordered ---unique--- items.
## Sets are useful for membership tests.
## Sets are also useful for duplicate elimination.
tech_books = {'abc', 'def', 'ghi','ghi'}
tech_stock = set([123,423,121])
tech_stock
123 in tech_stock

'''
                #######  2.3 Formatting
f-string -- The part {expression:format} is replaced.
Format codes (after the : inside the {}) are similar to C printf(). Common codes include:
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)
'''
name = 'ibm'
shares = 100
price =91.11
f'{name:>10s}{shares:>10d} {price:>10.2f}'

s = {       #dict
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
'{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
## using format method

## C-Style formatting
print('price of apple in fruticana is %d cent' %99)     ##note there is no ' ,' and there is % to fetch value
print('price of %s in fruticana is %f %s' %('apple', 99.9, 'cent'))

## f format doc https://docs.python.org/3/library/string.html#format-specification-mini-language
value = 4323.1004
print(f'{value:0.4f}')
print(f'{value:2.2f}')
print(f'{value:12.2f}')
print(f'{value:>12.2f}')
print(f'{value:<12.2f}')
print(f'{value:$^12.2f}')
print(f'{value:$>12.2f}')

'''
2.4 Sequences: Python has three Seq data types - 
    String  ''
    List    []
    Tuple   ()
 > All sequences are ordered, indexed by integers, and have a length.
 > Sequences can be replicated: s * n.
 > Sequences of the same type can be concatenated: s + t.
 > Slicing of a sequence - s[start:end]
'''

## Exercise 2.13: Counting
### range(): looping over sequence 
for i in range(10,20):
    print(i)

for n in range(10,0,-1):       # Count 10 ... 1
        print(n, end=' ')

for i in range(0,10,1):       # Count 10 ... 1
        print(i, end=' ')

### enumerating over sequence
names = ['aa','bx','dfds','zee']
for i,val in enumerate(names):
    print(i,val)

for i in enumerate(names):
    print(i)
    type(i)
    lst=list(i)
    print(lst, type(lst))
    tu = tuple(i)
    print(tu, type(tu))
    dct = {}
    dct[i[0]] = i[1]
    print(dct, type(dct))

### zip() function
# combines multiple sequences and makes an iterator that combines them
names = ['aa','bx','dfds','zee']
price = [22.22,43.53,6436.77,45.34]

shares = zip(names,price)                   # cobines and results in iterator
shares_list = list(zip(names,price))        #converts zip list iterator to list
for col,val in shares:
    print(col,val)

# Exercise 2.15: A practical enumerate() example
'''
Recall that the file Data/missing.csv contains data for a stock portfolio, but has some rows with missing data. 
Using enumerate(), modify your pcost.py program so that it prints a line number with the warning message when it 
encounters bad input.
'''
import os
import csv
workdir = os.getcwd()
workdir += r'\work\data'
with open(workdir+r'\missing.csv','rt') as f:
     rows = csv.reader(f)
     for i,row in enumerate(rows):
          try:
            for val in row:
                 if len(val) <= 0:
                    raise ValueError                                
            print(i, ' ', row, ' ')
          except ValueError:
               print(f'## Row {i}: Bad row:{row}')

##Exercise 2.16: Using the zip() function
'''
'''
import os
import csv
workdir = os.getcwd()
workdir += r'\work\data'
holding =[]
zholding=[]
hdr = ['name','shares', 'price','current price', 'purchase cost', 'current cost','gain/loss']
with open(workdir +r'\portfolio.csv','rt') as f, open(workdir +r'\prices.csv','rt') as g:
    rows = csv.reader(f)
    header = next(rows)    
    for i,row in enumerate(rows):                
        print(f'i={i} " " {row}')
        g.seek(0)
        prices = csv.reader(g)
        for item in prices:
           # print(item)
            #strx = item.split(',')
           # print("strx =", strx)
            if row[0] == item[0]:
                #print('******match', row[0] ,item[0])                
                status = row                
                cur_price = float(item[1])
                pur_cost = float(row[1])* float(row[2])
                cur_cost = float(row[1])* float(cur_price)
                gain_loss = cur_cost - pur_cost
                temp = [cur_price,pur_cost,cur_cost,gain_loss]
                status += temp
                print('--> in')
                zst = list(zip(hdr, status))
                zholding.append(zst)
                holding.append(status)
                break
    

print("#------------Report -----------------#\n")
print(hdr)
for i, share in enumerate(holding):    
        print( f'{i} {share}\n')

print("#------------Report2 -----------------#\n")
print(hdr)
for i, share in enumerate(zholding):    
        print( f'{i} {share}\n')


## Exercise 2.17: Inverting a dictionary using zip()
##Note-- When used in comparisons, tuples are compared element-by-element starting with the first item.
##    -- zip() is often used in situations like this where you need to pair up data from different places. 
##      -- Also, be aware that zip() stops once the shortest input sequence is exhausted.

prices = {
        'GO':55,
        'MS':33,
        'fb':66
}

# to get list of value key
price_list = list(zip(prices.values(),prices.keys()))
price_list
v,k = price_list[0]
print(sorted(price_list))
a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6]
list(zip(a, b, c))


'''##                             ##'''
##        2.5 collections module    ##
'''##                             ##'''

# tabulate total shares of each stock

portfolio = [
    ('GOOG', 100, 490.1),
    ('GOOG', 120, 390.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44),
    ('GE', 150, 83.44),
    ('GE', 100, 76.44),
    ('GOOG', 67, 290.1)
]

# use counter() object from collections module
from collections import Counter
total_shares = Counter()
for name,shares,price in portfolio:
    total_shares[name] +=shares

total_shares['GE']

# using defaultdict


'''##                             
##       2.6 List Comprehensions    ##
[ <expression> for <variable_name> in <sequence> if <condition>]
#A common task is processing items in a list. This section introduces list comprehensions, a powerful tool for doing just that.
'''##                            

# A list comprehension creates a new list by applying an operation to each element of a sequence
#Creating new lists
a = [1,2,3,4,5 , -10,22,12,6]
b = [2*x for x in a]
b

nameX = [nm.upper() for nm in names]
nameX

#Filtering
xt = [print(x) for x in a if x>0]
xt

## first run report.py program in bash/powershell mode and then try 


## set comprehennsion
## using { } bracket for this
xt = { print(s) for s in zholding}
xt = { print(s) for s in holding}
xt


'''##                             
##       2.6 Objects    ##

'''##   
# Assignment
# assignment operations never make a copy of the value being assigned. 
# All assignments are merely ****reference copies**** (shallow copy or copy by reference or * assignment) (or pointer copies if you prefer).
# to check the two assigned values; use "is" or "==" to compare eg: a is b or a == b
## shallow copy
a = [2,3,4]
b =a
b
a.append(5)
a
b
b.append(0)
a
b
c = b
b[1] == a[1]
# Reassigning values
# Reassigning a value never overwrites the memory used by the previous value.
a = [9,9,9,9]
a
b
a is b      # compares not the value by the pointer/reference address

id(a) == id(b)
id(a)
id(b)
id(c)

## deep copy
# use copy module
import copy
a = [2,4,[55,66]]
b = a
a
b
a == b
a[2].append(99)
a
b

b = copy.deepcopy(a)
a
b
a == b
a[2].append(100)
a
b
a[2] == b[2]

## Type Checking for an object -- isinstance()
a = [2,3,4]
type(a)
isinstance(a, list)
'''
Everything is an object
Numbers, strings, lists, functions, exceptions, classes, instances, etc. are all objects. 
It means that all objects that can be named can be passed around as data, placed in containers, etc., 
without any restrictions. There are no special kinds of objects. Sometimes it is said that all objects are “first-class”.
'''
import math
import os
items = [abs, math, copy, os, ValueError, 1, "strd", {"age":23}, (32,4)]
items

'''
Exercise 2.24: First-class Data
'''
import os
import csv
workdir = os.getcwd()
workdir += r'\work'
types =[str,int,float]
with open(workdir+r'\data\portfolio.csv') as f:
    rows = csv.reader(f)
    hdr = next(rows)    
    shareValue =0
    for row in rows:       
       r = zip(types,row)
       print(list(r))
       shareValue += types[1](row[1])*types[2](row[2])
    print(f'total share value = {shareValue}')

##2 -- more useful to pase data; use types and then use zip. new thing is using "fun" function type
types =[str,int,float]
with open(workdir+r'\data\portfolio.csv','rt') as f:
    rows = csv.reader(f)
    hdr = next(rows)    
    shareValue =0
    shareValue2 =0
    allData = []
    dataDict = []
    for row in rows:       
        converted = []
        for fun, val in zip(types,row):     #In the loop, the func variable is one of the type conversion functions       
           converted.append(fun(val))       # this can also be done wtih - { name: func(val) for name, func, val in zip(headers, types, row) }        
        shareValue2 += converted[1]*converted[2]
        d= dict(zip(hdr,converted))
        dataDict.append(d)
        allData.append(converted)
        shareValue += types[1](row[1])*types[2](row[2])
    print(f'total share value = {shareValue}  {shareValue2}')       

for x in allData:
    print(x)

##2 - using list comprehension to do similar 
f = open(workdir+r'\data\dowstocks.csv','rt')
rows =csv.reader(f)
hdr = next(rows)
types = [str, float, str, str, float, float, float, float, int]
for row in rows:
    convertedX= [fun(val) for fun,val in zip(types,row)]
f.close()