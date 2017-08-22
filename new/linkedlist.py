class slist:
    class _Node:
        def __init__(self,element):
            self.data=element
            self.next=None
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def isempty(self):
        return self.count==0
    def length(self):
        return self.count
    def first(self):
        if not self.isempty():
            return self.head.data
    def last(self):
        if not self.isempty():
            return self.tail.data
    def add_first(self,val):
        new_node=self._Node(val)
        if not self.isempty():
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1
    def add_tail(self,val):
        new_tail=self._Node(val)
        if not self.isempty():
            self.tail.next=new_tail
            self.tail=new_tail
        else:
            self.head=self.tail=new_tail
        self.count+=1
    def del_first(self):
        if not self.isempty():
            data=self.head.data
            self.head=self.head.next
            if self.head is None:
                self.count+=1
            return data
    def del_last(self):
        if not self.isempty():
            data=self.tail.data
        if self.count==1:
            self.head=self.tail=None
        else:
            last=self.tail
            cur=self.tail
            while cur.next is not last:
                cur =cur.next
            self.tail=cur
            self.tail.next=None
        self.count-=1
        return data
    def ismember(self,key):
        if not self.isempty():
            cur =self.head
            while cur is not None:
                if cur.data==key:
                    break
                else:
                    cur=cur.next
            return cur!=None
    def max(self):
        if not self.isempty():
            cur=self.head
            maximum=self.head.data
            while cur is not None:
                if cur.data>maximum:
                    maximum=cur.data
                cur=cur.next
            return maximum
    def min(self):
        if not self.isempty():
            cur=self.head
            minimum=self.head.data
            while cur is not None:
                if cur.data<minimum:
                    maximum=cur.data
                cur=cur.next
            return minimum
    def add_element(self,key1,key2):
        if not self.isempty():
            cur =self.head
            c=0
            while cur is not None:
                c+=1
                if cur.data==key1:
                    break
                else:
                    cur=cur.next
            new_node=self._Node(key2)
            new_node.next=cur.data
            cur=new_node
    def display(self):
        if not self.isempty():
            cur=self.head
            while cur is not None:
                print(cur.data)
                cur=cur.next
        
