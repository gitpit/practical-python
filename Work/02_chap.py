'''
# Working with Data
https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/00_Overview.html
'''
##### 2.1 Datatypes and Data structures

## none type: None is often used as a placeholder for optional or missing value. It evaluates as False in conditionals.
email_addr = None

## Tuples - collection of values grouped together. represent simple records or structures.
## A good analogy: A tuple is like a single row in a database table.
## Contents are ordered but can not be modified

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

s = { 'id':'Id11',
      'age':22,
      'Gender': 'F'
    }

print(s['id'])

# excercise
import os
import csv

fpath = os.getcwd()
fpath += r'\work\data\portfolio.csv'
with open(fpath,'rt') as f:
    rows =csv.reader(f)
    z =next(rows)
    r = next(rows)
    print(r)
    (a,b,c)  = next(rows)
    