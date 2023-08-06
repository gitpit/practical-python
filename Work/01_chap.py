# comment line in python
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
#
'''
In interactive mode, The underscore _ holds the last result. Nevre use in a program

'''
#

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

'''
## Strings
## strings are immutable in python

'''
a = "hello world"
x = a[2]
x = x+ "hello"
print(x)

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

''' 
## raw strings
'''
rs = r'c:\newdata\test'
rs1 = 'c:\newdata\test'
print(rs)
print(rs1)

## byte tring
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
