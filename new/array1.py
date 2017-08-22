class ArrayStack:
    default_capacity=2

    def __init__(self):
        self.count=0
        self.ls=[]
    def isfull(self):
        return ArrayStack.default_capacity==self.count
    def push(self,k):
        if not self.isfull():
            self.ls.append(k)
            self.count+=1
        else:
            return False
    def isempty(self):
        return self.count==0
    def pop(self):
        if not isempty():
            self.count-=1
            return ls.pop()
