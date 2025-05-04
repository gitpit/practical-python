import os
import sys
import csv
#ask for input file path to show
#input file path and 
# read text, csv file and output data
#

dpath = os.getcwd()
dpath += r'\work\data'
print(dpath)

# print("enter .txt file name to read and print")
# tfile =input()
# dpath1 = dpath+'\\'+tfile
# print(dpath1)

# with open(dpath1,'r') as f:
#     data =f.read()
#     print(data)

# playing with class and stuff
class XMesSec:
    # def __init__(self) -> None:
    #     pass
    def __init_subclass__(self,z,x,y,d) -> None:
        self.z = z
        self.x=x
        self.y=y

class XMesLog:
    def __init__(self,logid,seg, size, msec) -> None:
        self.logid =logid
        self.seg = seg
        self.size = size
        self.sections = msec

#reading and storing logs and printing 

def ReadMesLogs(mesfile):
    print("reading mes file f{mesfile} ---\n")
    logs =[]
    with open(mesfile, 'r') as f:
        header =f.readline()
        hdr = header.split()
        logname = hdr[0]
        seg = hdr[1]
        size = hdr[2]
        print(header)
        sec =[]
        for line in f:
            xd = line.split()
            s1 = XMesSec(xd[0],xd[1],xd[2])
            print('\n')
    print("--------done---------\n")
        

print("enter .csv file name to read and print")
tfile =input()
dpath2 = dpath+'\\'+tfile
print(dpath2)

# with open(dpath2,'r') as f:
#     lines =csv.reader(f)
#     for line in lines:
#         print(line)

ReadMesLogs(dpath2)
print("here!!")