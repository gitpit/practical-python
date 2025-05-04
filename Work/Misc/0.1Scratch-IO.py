#test code
import os
import sys
import time
import random
import string
import math
import re
import json

wdir = os.getcwd()
wdir = wdir +r'\work\data'
fooFile = wdir +r'\foo.txt'
print(wdir)
# Open the file in read mode
with open(fooFile, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
    print(file_contents)
# Print the contents of the file

portFile = wdir + r'\portfolio.dat'
print("\n========================\n")
# Open the file in read mode
with open(portFile,'r') as file:
    for line in file:
        # Print each line
        print(line.strip())

#read file using csv reader
print("\n============xxxx============\n")

import csv
with open(portFile,'r') as cfile:
    rows = csv.reader(cfile)
    for row in rows:
        print(row)
#read file using pandas
#import pandas as pd