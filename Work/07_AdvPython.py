'''
7.1 Variable argument functions
7.2 Anonymous functions and lambda
7.3 Returning function and closures
7.4 Function decorators
7.5 Static and class methods
'''

##7.1 Variable argument functions

###Positional variable arguments (*args)
###
def f(x,*args):
    print('x ={%d}'%x)
    for a in args:
        print(a)
f(1,2,3,4,5)

### Keyword variable arguments (**kwargs)
###
def f2(x,**kwargs):
    print('x ={%d}'%x)
    for a in kwargs:
        print(a)

f2(4,mode='fast',flag=False,hdr="what")

### Passing Tuples and Dicts
###
nums=(1,2,3,4)
nums2=(11,22,33,44)
f(0,nums,nums2)


d1 ={
    'x':2,
    'y':2.2,
    'z':99
}

f(12,d1)

#average of nums
def avg(*args):
    av = sum(args)/len(args)
    print(f'average=%d'%av)

avg(1,2,3,4,5)

'''scratch code test  15 min code
read meslog.txt
'''
def read_meslog(filename):
    sections=[]
    print(filename)
    sections = []
    logs = []
    with open(filename,'r+') as f:
        hdr =f.readline()
        hdr = hdr.split()
        print(hdr)
        print(hdr[0])
        print(hdr[1])
        print(hdr[2])
        if hdr[0] != '.' and hdr[1] != '.'and hdr[2] != '.':
            id,lno,nsecs=str(hdr[0]),int(hdr[1]),int(hdr[2])
            #print(f'id=%s , sections=%d'%(id,secs))
        i =0
        while i < nsecs:
            line =f.readline()
            line = line.split()
            xs =XSec(line[0],line[1],line[2],line[3])
            print('\t',line)
            sections.append(xs)
            i +=1
        lgs = XLog(hdr[0],sections)
        logs.append(lgs)
    return logs
        

## 2nd card; use a quick class

class XSec:
    def __init__(self,z,x,y,d):
        #instance data
        self.z=z
        self.x =x
        self.y=y
        self.d =d  #dia
    #special methods
    def __str__(self):
        return f'{self.z} {self.x}  {self.y}  {self.d} '

class XLog:
    def __init__(self,lid,xs) -> None:
        self.logId = lid
        self.secs =xs

        
import os
import sys
data_dir = os.getcwd()
data_dir += r'\work\data'
mesfile_path= data_dir + r'\meslogs1.txt'
mesfile_path
xlogs = read_meslog(mesfile_path)

print("\n\n")

for lg in xlogs:
    print(lg.logId)
    for x in lg.secs:
        print(x)

x1 = [1,3,4]


### 7.2 Anonymous Functions and Lambda

import queue
q1 =queue.Queue()
q1.put(11)
q1.put(12)
q1.put(13)
while( q1.qsize() !=0):
    print(q1.get())


st = stack_data.s