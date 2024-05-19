'''
# 4.0 Class & Object
4.1 Introducing Classes
4.2 Inheritance
4.3 Special Methods
4.4 Defining new Exception
'''
# class statement
# The object is always passed as the first argument. It is merely Python programming style to call this argument self
class Player:
    def __init__(self, x, y):       # like c++ constructor
        self.x = x
        self.y = y
        self.health = 100
    '''
    def __init__(self):             # check about default constructor
        self.x =0
        self.y=0
    ''' 
    def move(self, dx, dy):         # self is the instance or similar to this pointer in c++
        self.x += dx
        self.y += dy
  
    def damage(self, pts):
        self.health -= pts

a = Player(2,4)
b = a
print(a.x)
print(b.x)
a.x = 19
print(a.x)
print(b.x)
c = Player()
print(c.x)

## class scoping
#Classes do not define a scope of names.; use "self" to call any instance method otherwise global method is called.

'''
Set excercise path to lookup python module

#locating modules
import sys
import os

excdir = os.getcwd()
excdir += r'\work\Excercise\4.1\'
sys.path
sys.path.append(excdir)
'''
#import stock
import sys
import os

excdir = os.getcwd()
excdir += r'\work'
sys.path
sys.path.append(excdir)

from stock import Stock

a = Stock('goo',11,22.22)
b = Stock('uuu',66,77.23)

#-------------------------------------------
# importing Tlogs module and printing....
import Work.meslog as meslog
dataDir = os.getcwd()
dataDir += r'\work\Data\meslogs.txt'
mylogs = meslog.ReadMesLogs(dataDir)


for log in mylogs:
    #print(log.Id)
    #str(log)
    for sec in log.sections:
        #print(sec.z,sec.x,sec.y,sec.d)
        print(str(sec))
    print('---------------')


#----------------------------------
    
stc = [a,b]
stc
for s in stc:
    print(s.name,s.price)

for i,s in enumerate(stc):
    #print(i,s.name)    
    print(s)

##Exercise 4.2: Adding some Methods
# add few more methods....cost, sell, buy

a.shares
a.cost()
a.sell(10)
a.buy(10,22.22)

# Exercise 4.3: Creating a list of instances
import fileparse
import os

workdir = os.getcwd()
workdir += r'\work'
#with open(workdir+r'\data\portfolio.csv','rt') as f:
portDict = fileparse.parse_csv2(workdir+'\data\portfolio.csv')

stocks1 =[]
for d in portDict:
    #s =Stock(d['name'],int(d['shares']),float(d['price']))
    stocks1.append(Stock(d['name'],int(d['shares']),float(d['price'])))

stocks2=[Stock(d['name'],int(d['shares']),float(d['price'])) for d in portDict]


for st in stocks2:
    print(st.name,st.shares,st.price)

sumval =sum([s.cost() for s in stocks2])
print(sumval)
#Exercise 4.4: Using your class
# inside report.py



'''                            
            ########### 4.2 inheritance
    class Parent:


    class Child(Parent):
    >>> with Inheritance
        Extending :  With inheritance, you are taking an existing class and:
            Adding new methods
            Redefining some of the existing methods
            Adding new attributes to instances  

    >>> method overriding can be done
        using "super" to call the base class method

    class Stock:
        ...
        def cost(self):
            return self.shares * self.price
        ...
    class MyStock(Stock):
        def cost(self):
            # Check the call to `super`
            actual_cost = super().cost()        ## using super ...
            return 1.25 * actual_cost

    >>> if __init__ is redifined in derived class, it is essential to initialize parent
        call the __init__() method on the super which is the way to call the base version as shown previously.
    >>> object as base class - if a class has no parent, object can be used as a base class. "object" is the parent of all objects in Python
    >>> Multiple inheritance
    class Mother:
    ...
    class Father:
    ...
    class child (Mother, Father):
'''

'''
Exercise 4.5: An Extensibility Problem
source file tableformat.py
abstract class; only declaration for extensibility
Exercise 4.7: Polymorphism in Action

''' 

from stock import Stock,MyStock

ms = MyStock(20,120,2)
print(ms.cost())

s2 = ms.cost
s2
s2()

'''
    4.3 Special Methods
    -------------------
    Classes may define special methods which are treated special way by the python interpreter.
    Special methods are always preceded by __; eg: __init(self):
'''
from datetime import date
d = date(2024,11,12)
print(d)

str("str")
str(d)
repr(d) # __repr__

#todo:: try using special function str and __len__; __getitem__()

# lookup and bound methods
lg1 = meslog.TSec(2,3,4,5)
lg1
lg1()

## Attribute Access
'''
property getter and setter
'''

        ###### 4.4 Defining Exceptions

class NetworkError(Exception):
    pass

class AuthenticationError(NetworkError):
    pass


