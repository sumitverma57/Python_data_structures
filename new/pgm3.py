class ArrayStack:
    max_len=10
    def __init__(self):
        self.count=0
        self.data=[]
    def isfull(self):
        return LimitedStack.stack_capacity==self.count
    def push(self,key):
        try:
            if not self.isfull():
                self.data.append(key)
                self.count+=1
        except:
            print("FULL")
    def isempty(self):
        return self.count==0
    def pop(self):
        if not self.isempty():
            self.count-=1
            return self.data.pop()
    def length(self):
        return self.count
    def peak(self):
        if not self.isempty():
            return self.data[-1]
