'''
###         5. Inner workings of Python Objects         ####

'''

#####  5.1 Dictionaries Revisited
'''
Dicts and Modules
Within a module, a dictionary holds all of the global variables and functions.
'''
#import meslog
import sys
import os

excdir = os.getcwd()
excdir += r'\work'
sys.path
sys.path.append(excdir)
import Work.meslog as meslog

xs =meslog.TSec(1,2,3,4)
xs.__dict__

'''
### Dicts and Objects
User defined objects also use dictionaries for both instance data and classes. In fact, the entire object system is mostly 
an extra layer that’s put on top of dictionaries.

A dictionary holds the instance data, __dict__.
'''
import stock

s1 = stock.Stock('gg',12,45)

s1.__dict__

'''
####    5.2 Classes and Encapsulation
'''
# public vs private variable
# any attribute with leading _ is private in python but only as style. In python everything is visible.
class person:
    def __init__(self) -> None:
        self._name=0

# one can defie accessor methods as like c++, C#; and raise a typeerror exception...

## defining Properties      @property
class XStock:
    def __init__(self,nm,sh,pr):
        self.name=nm
        self.shares=sh
        self.price = pr
    @property
    def shares(self):
        return self._shares     # note -- property uses private name with _
    @shares.setter
    def shares(self,value):
        if not isinstance(value,int):
            raise TypeError('expected int')
        self.shares = value


s1 = XStock('gg',12,343.1)
s1.name
s1.shares
s1.gox =20
s1.gox

## using __slots__ to fix set of attributes belonging to an object; without this, attribute can be added to an object at run time

class YStock:
    __slots__ =('name','_shares','price')
    def __init__(self,nm,sh,pr):
        self.name=nm
        self._shares=sh
        self.price = pr
    @property
    def shares(self):
        return self._shares     # note -- property uses private name with _
    @shares.setter
    def shares(self,value):
        if not isinstance(value,int):
            raise TypeError('expected int')
        self.shares = value

s2 = YStock('gg',12,343.1)
s2.name
s2.shares
#s2.gox =20      # uncomment - it should fail bocz of slots
s2.gox