'''
6. Generators
6.1 Iteration Protocol
6.2 Customizing Iteration with Generators
6.3 Producer/Consumer Problems and Workflows
6.4 Generator Expressions
'''
## 6.1 Iteration Protocol

a = 'hello'
for c in a: # Loop over characters in a
    print(c)

b = { 'name': 'Dave', 'password':'foo'}
for k in b: # Loop over keys in dictionary
    print(k)
for k,v in b.items(): # Loop over keys and values in dictionary
    print(k,v)


## using hash function
    #https://stackoverflow.com/questions/4567089/hash-function-that-produces-short-hashes
import hashlib
import base64
plaintext1 ="long_namexyz_1234567892"
hash_result1 = hashlib.sha256(plaintext1.encode()).digest()[:16]
hash_result1
hash_result2 = hashlib.shake_256(plaintext1.encode()).hexdigest(4)
hash_result2
#encoded_result = base64.b64decode(hash_result1).decode('UTF-8')  #base64.b64encode(hash_result1).decode("utf-8")
#encoded_result 

'''
6.2 Customizing Iteration ---- GENERATORS ----- using yield

## Generators -A generator is a function that defines iteration
## A generator is any function that uses the yield statement. Calling a generator function creates a generator object. 
## It does not immediately execute the function.
'''
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(10):
    print(x, end=' ')

y = countdown(5)


for i in y:
    print(i)

# Exercise 6.4: A Simple Generator  filematch check

def quickLines(filename):
    print(filename)
    for line in open(filename,'r'):
        print(line, end=' ')


def filematch(filename,substr):
    with open(filename,'r') as f:
        for line in f:
            if substr in line:
                yield line


import os
import pathlib

workdir = os.getcwd()
datadir = workdir + r'\work\data'
quickLines(datadir+r'\portfolio.csv')

print('\n ----\n')


for x in filematch(datadir+r'\portfolio.csv','IBM'):
    print(x)

########
#######     6.3 Producers, Consumers and Pipelines
######## producer → processing → processing → consumer

## Generator Pipelines

## Exercise 6.8: Setting up a simple pipeline
## producer → processing → processing → consumer
def filematch(lines,substr):
    for line in lines:
        if substr in line:
            yield line
                

from follow import follow
import os
import time

datadir = os.getcwd() + r'\work\data'
stocklogFile = datadir + r'\stocklog.csv'
lines = follow(stocklogFile)    #processing

ibm = filematch(lines,'IBM')    #processing

for line in ibm:        #consumer
    print(line)


##Exercise 6.9: Setting up a more complex pipeline
from follow import follow
import csv

lines = follow(stocklogFile)

for row in csv.reader(lines):
    print(row)