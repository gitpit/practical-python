'''
# log class
'''
class TSec:
    def __init__(self,z,x,y,d):
        #instance data
        self.z=z
        self.x =x
        self.y=y
        self.d =d  #dia
    #special methods
    def __str__(self):
        return f'{self.z} {self.x}  {self.y}  {self.d} '

class TLog:
    def __init__(self,id,seg,sz,xs):
        self.Id=id
        self.segNum=seg
        self.size=sz
        self.sections=xs
    #using special method __str__
    def __str__(self):
        return f'{self.Id}\t{self.segNum}\t{self.size}\t\n'

def ReadMesLogs(mesfile):
    '''
    reads mes file and returns log list
    '''
    logs = []       # list of logs
    print(mesfile)
    with open(mesfile, 'r') as f:
        for line in f:
            #hdr = f.readline()
            strs = line.split()            
            if len(strs) >=4 and strs[0] != '.' and strs[1] != '.' and strs[2] != '.' and strs[3] != '.':                
                id,seg,nsec,wgt = strs[0],int(strs[1]),int(strs[2]),float(strs[3])
            i=0
            secs = []
            while i < nsec:     # read all section for the log
                line = f.readline()
                line = line.split()
                xs = TSec(float(line[0]),float(line[1]),float(line[2]),float(line[3]))
                secs.append(xs)
                i +=1
            #complete a log and append to logs
            logs.append(TLog(id,seg,nsec,secs))
    return logs

# Main function
def main():
    import os
    dataDir = os.getcwd()
    dataDir += r'\work\Data\meslogs.txt'
    mylogs = ReadMesLogs(dataDir)
    for log in mylogs:
        print(log.Id)
        for sec in log.sections:
            print(sec.z,sec.x,sec.y,sec.d)
        print('######')


if __name__ == '__main__':
    main()