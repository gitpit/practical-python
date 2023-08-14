'''
# Chap 2: Working with Data
https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/00_Overview.html
'''
        ##### 2.1 Datatypes and Data structures

## none type: None is often used as a placeholder for optional or missing value. It evaluates as False in conditionals.
email_addr = None

    ## Tuples - collection of values grouped together. represent simple records or structures.
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
2.2 Containers
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