#scrath file... delete/rub off
'''
take input from console upto 10 lines
'''
print('test')

import os
workdir = os.getcwd()
workdir += r'\work'
datadir = workdir + r'\data'

with open(datadir+r'\1idata.txt','w+') as ifs:
    i=0
    lines=[]
    ifs.write('#header for the test file\n')
    while i <5:
        line =input(f'Enter line {i:2d}:')        
        i+=1
        lines.append(line)
        ifs.write(line + '\n')
    ifs.write('# End header for the test file\n')

with open(datadir+r'\1idata.txt','rt') as ifs, open(datadir+r'\1odata.txt','w+') as ofs:
    for line in ifs:
        print(line)
        next(ifs)
        ofs.write(line)

print('done temp printing stuff')

for line in lines:
    print(line)

with open(datadir+r'\1odata.txt','w+') as ifs:
    for line in ifs:
        print(line)
