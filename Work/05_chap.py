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