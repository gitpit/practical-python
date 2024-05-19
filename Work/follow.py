'''
## Exercise 6.5: Monitoring a streaming data source
## Iterator Generator (yield) example
'''
### --> first run stocksim.py in a seperate window and then run below program
import os
import time
def follow(filename):
    f = open(filename)
    f.seek(0,os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue              
        yield line
        
print("\n###################\n")
datadir = os.getcwd() + r'\work\data'
stocklogFile = datadir + r'\stocklog.csv'

'''
    for line in follow(stocklogFile):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        prev =  float(fields[5])
        change = float(fields[4])
        if change < 0:            
            print(f'{name:>10s} {price:>10.2f} {prev:>10.2f} {change:>10.2f}')
            #print(line)

'''


