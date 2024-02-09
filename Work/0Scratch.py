#scrath file... delete/rub off
'''
take input from console upto 10 lines
'''
print("read a csv file and pring to another file")
import os

fpath = os.getcwd()
fpath += r'\work\Data\foo.txt'

with open(fpath,'r') as f:
    data =f.read()
    print(data)
    f.seek(0)
    for line in f:
        print(line)
        print('---------------\n')