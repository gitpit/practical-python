############# chap-1 #################
# comment line in python
#https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/04_Strings.html
'''
 #Python: It’s All About the Indentation
 indentation is used to define compound statements or blocks. In a Python program, contiguous statements that are indented to the same level are considered to be part of the same block.
 https://realpython.com/python-conditional-statements/#python-its-all-about-the-indentation

 if <expr> :
    <stmt> 
    <stmt> -- block ends
else
    <stmt>  -- block ends

while <expr> :
    <block in same indentation>
'''
print("test")
## below code doesn ot work
'''
import urllib.request
webUrl = urllib.request.urlopen('https://www.javatpoint.com/python-tutorial')  
u = urllib.request.urlopen ('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22','dfd', 11)
u1 = urllib.request.urlopen('https://www.javatpoint.com/python-tutorial')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)
'''

'''
In interactive mode, The underscore _ holds the last result. Nevre use in a program

'''
# simple excercise

bill_thickness = 0.11 #meters
tower_height = 99999  #meters
day = 1
num_bills =1
while num_bills*bill_thickness < tower_height :
    print(day,num_bills,num_bills*bill_thickness)
    day +=1
    num_bills *=2
print('number of days',day)
print('number of bills', num_bills)
print('final height', num_bills*bill_thickness)

'''
learn few thigns from above example
 types      variables   comments    indentation     code block     loop     case sensitive-python is case sensitive language    conditional statement (if else)
 In a print, extra line can be supressed
 The extra newline can be suppressed: 
 print('Hello', end=' ')
print('My name is', 'Jake')

##user input
name = input('enter name')
print('your name is',name)

##pass statement
Sometimes you need to specify an empty code block. The keyword pass is used for it.
if a > b:
    pass
else:
    print('Computer says false')

## numbers test
float 
int
booleans

## operators
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide (produces a float)
x // y     Floor Divide (produces an integer)
x % y      Modulo (remainder)
x ** y     Power
x << n     Bit shift left
x >> n     Bit shift right
x & y      Bit-wise AND
x | y      Bit-wise OR
x ^ y      Bit-wise XOR
~x         Bit-wise NOT
abs(x)     Absolute value

## comparison
x < y      Less than
x <= y     Less than or equal
x > y      Greater than
x >= y     Greater than or equal
x == y     Equal to
x != y     Not equal to

## Converting Numbers
a = int(x)    # Convert x to integer
b = float(x)  # Convert x to float

>> solve dave's mortagage

'''
principal = 500000.0
rate = 0.05
overperiod = 30
payment = 2684.11
total_paid = 0.0
interest = 0.0
month = 1
extraPaid = 1000
forMonths = 12
while principal > 0:
    if forMonths > 1:
        principal = principal - extraPaid
        forMonths -=1     
    principal = principal * (1 +rate/12 ) - payment
    total_paid = total_paid + payment
    print ('month - principal', month, principal)    
    month +=1
   
print('total paid', total_paid)    
print('hello')


'''######### 1.4 Strings ##########
# strings are array of chars
# Strings are “immutable” or read-only. Once created, the value can’t be changed.
# but string variable can be reassigned. (something like const pointer and point to constant in C)
# 'in' is a operator in python can be applied in strings
# strings can be read forward and backward (-2)
'''
## raw strings
rs = r'c:\newdata\test'
rs1 = 'c:\newdata\test'
print(rs)
print(rs1)

'reverse string'
name = "prakash"
count = len(name)
print(count/2)
i =0
name1 = ''
while i < round(len(name)):    
    name1 = name1 + name[count-i-1]
    i +=1
    
print(name)
print(name1)
name = 'zyxmo'
name1 =''
for x in reversed(name):
    name1 +=x
print(name1)

## byte string, unicode etc.
bstr = b'hello'
len(bstr)
bstr1 = 'hello'
len(bstr1)
money = 1001.212
## formatted string printing
print(f'{name:10s} {money:5.2f}')

## excercises
symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
symbols[0]
symbols += ',GOOG'
print(symbols)

# using in operator
'IBM' in symbols
'BM' in symbols

## using string methods
'''
dir() produces a list of all operations that can appear after the (.). 
Use the help() command to get more information about a specific operation:

'''
dir(symbols)
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
   'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
   'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
     'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 
     'zfill']
'''
help(name.upper)
symbols.lower()
symbols.find('IB')
symbols[5:15]

## format string f-strings
'''
Sometimes you want to create a string and embed the values of variables into it.
'''
#examples
tshare ='xyx corp'
price=999.903
sym = 'xy'
f'{tshare} with range{sym} amount {price:0.2f}'

## Exercise 1.18: Regular Expressions
'''
use pythong re module for regular expressions
import re
more info: https://docs.python.org/library/re.html
'''
text = 'Today is 08/06/2023. Tomorrow is 08/07/2023.'
 # Find all occurrences of a date
import re
re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
# Replace all occurrences of a date with replacement text
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
text

'''######### 1.5 Lists [ ] ##########
Python’s primary type for holding an ordered collection of values.
Use square brackets     [  ] to define a list literal:
Index stats from 0 and Negative indices count from the end.
You can change any item in a list.
# list can have heterogenous itmes
'''
names = ['tim', 'tom','bib', 'bob']
dir(names)
## Sometimes lists are created by other methods. For example, a string can be split into a list using the split() method
line = 'jab tab kab kab'
listline = line.split()
listline
## list operations
names.append('alice')
names.insert(2,'malroy')
miscNames = ['jack', 'jill']
names = names + miscNames
names[4] = 'Mills'
len(names)
'jack' in names     # using in operator
'bob' not in names  # using not in operator
# replication; 
it = [1,2,3,4]
it = it *3              #here list is replicted three times
# list iteration
for name in names:
    print(name)

# removing from list using remove('item') or del names[1]
# Lists can be sorted “in-place”.
names.sort()
#Use sorted() if you’d like to make a new list instead:
t = sorted(names)

## taking list of string and join them into a string
ts = ','.join(names)
ts
type(ts)
type(names)
## list of list and 
tx = ['test1',names,it]

for item in tx:
    print(item)
    next(tx)

'''######### 1.6 File Management   ##########
open file should be closed
'''
## Open a file and read data and write to bar.txt
import os
import pathlib
tp = os.getcwd()
# tp2 = pathlib.Path(__file__).parent.resolve()       ## __file__ it does not work in interactive mode; so run in file mode
f = open( tp+r"\Work\Data\foo.txt",'rt')
g = open(tp+r'\work\data\bar.txt', 'w+')

data = f.read()
g.write(data)
g.write('------------end -----------')
g.seek(0)
line = g.readline()
print(line)
while line:
    print(line)
    line = g.readline()

f.close()
g.close()

## another way read a line and write a line
f = open( tp+r"\Work\Data\foo.txt",'rt')
g = open(tp+r'\work\data\bar.txt', 'w+')

for dat in f:
    g.write(dat)
g.write('------------end2 -----------') 
g.seek(0) 
for d in g:
    print(d)
f.close()
g.close()

##  another way to open and close file without using close() method

with open( tp+r"\Work\Data\foo.txt",'rt') as f, open(tp+r'\work\data\bar.txt', 'w+') as g:
    for line in f:
        g.write(line)
    g.seek(0)
    for line in g:
        print(line)
    print("-- done file operation---")

## Redirect the print function to out
with open( tp+r"\Work\Data\foo.txt",'rt') as f, open(tp+r'\work\data\bar.txt', 'w+') as out:
    for line in f:
        print(line,file=out)
        ## skip one line in between
        next(f)        
    print("$$$$ output to console is set to file", file=out)
    out.seek(0)
    for line in out:
        print(line)


