'''
Write implementaton  for 
queue
stack
binary tree
'''
class TStack:
    def __init__(self,tp,size):
        self.top = tp     
        self.size =tp
        self.Max=size
        self.items =[]
    def IsEmpty(self):
        if(self.top ==-1):
            return True
        else:
            return False
    def IsFull(self):
        if(self.top == self.Max):
            return True
        else:
            return False
    def Push(self,e):
        self.top= self.top+1
        self.items.append(e)
    def Pop(self):
        x = self.items.pop(self.top)
        self.top = self.top-1
        return x
    
st =TStack(-1,10)
st.Push(5)
st.Push(15)
st.Push(125)
st.Pop()
st.Push(51)
st.Push(152)
st.Push(0)
while(not st.IsEmpty()):
    x1 = st.Pop()
    print(x1)

class TQueue:
    def __init__(self,sz):
        self.front=-1
        self.back = -1
        self.len =sz
        self.items=[]
    def insert(self,e):
        
## dfs implementation for a simple graph  -- with stack
## bfs implementation       -- with queue
##

