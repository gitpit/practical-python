'''
# Chapter 3: Program Organization - practice
# Dated:2023/10/06
'''

'''
3.1 Scripting
'''

#functions

def square_root(num):
    '''
    About square root 
    '''
    return num*num
square_root(44)

## to try... writing report.py program as a consolidated one

'''
3.2 More on Functions
'''
# default arguments
# If no return value is given or return is missing, None is returned.
# multiple reutrn value as tuple

#note:: function can't modify global variable outside
# to modify a global vairbale it has to prefix with global keyword inside its scope
name = 'Dave'
def spam():
    global name
    name = 'Guido' # Changes the global name above

# argument passing - pass by value ; pass by ref
## Key point: Functions don’t receive a copy of the input arguments.
## Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value.


# fileparse.py
#Reading CSV Files
# Exercise 3.3

## 3.3 Exception Handling -- 
## Error Checking

# raising an error
code = ['dfd2','32df','ffss','ggd']
cd ='ffs2s'
if cd not in code:
    raise LookupError(f'{cd} no there in list')
else:
    print("found")
# to catch an exception use try-except
# Exceptions propagate to the first matching except##
def foo(nm):
    try:       
        code.append('adfs')
        code[2] = '1233'
        print(code)
    except NameError as e:
        print(e)

foo(cd)
# Catching Multiple Errors
'''
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
'''
# Catching All Errors -To catch any exception, use Exception like this:
'''
try:
    ...
except Exception:       # DANGER. See below
    print('An error occurred')
'''

### finally statement
''' 
It specifies code that must run regardless of whether or not an exception occurs.
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.

with statement
In modern code, try-finally is often replaced with the with statement.
with open(filename)     as f:
with defines a usage context for a resource. When execution leaves that context, resources are released. 
with only works with certain objects that have been specifically programmed to support it.
'''

##todo excercise- 3.9 and 3.10



    ### 3.4 Modules
    ###
'''
 ** any python file is a module; module names is tied to file name

import fileparse
import report
import os
import csv
workdir = os.getcwd
workdir += r'\work'

recs = fileparse.parse_csv(workdir+r'\data\portfolio.csv')
'''
##### Namespaces
'''
A module is a collection of named values and is sometimes said to be a namespace. The names are all of the global variables 
and functions defined in the source file. After importing, the module name is used as a prefix. Hence the namespace.
'''


## import as statement
#You can change the name of a module as you import it:  -- like an alias
'''
Specifically, import always executes the entire file and modules are still isolated environments.

The import module as statement is only changing the name locally. The from math import cos, sin statement still loads 
the entire math module behind the scenes. It’s merely copying the cos and sin names from the module into the local space 
after it’s done.
Each module loads and executes only once. Note: Repeated imports just return a reference to the previously loaded module.
'''
import fileparse as fi
import math as m
fi.parse_csv()

def rectangle(r,theta):
    x = r*m.cos(theta)
    y = r*m.sin(theta)
    return x,y

#from module import
#This picks selected symbols out of a module and makes them available locally.
#
from math import sin,cos

#locating modules
import sys
sys.path
#sys.path.append(workdir)