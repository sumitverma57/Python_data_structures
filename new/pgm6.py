import stack
if __name__ == '__main__':
    R=stack.LimitedStack()
    S=stack.LimitedStack()
    T=stack.LimitedStack()
    temp1=stack.LimitedStack()
    temp2=stack.LimitedStack()
    R.push(1)
    R.push(2)
    R.push(3)
    S.push(4)
    S.push(5)
    T.push(6)
    T.push(7)
    T.push(8)
    T.push(9)
    while S.isempty()==False:
        h=S.pop()
        temp1.push(h)
    while T.isempty()==False:
        j=T.pop()
        temp1.push(j)
    while temp1.isempty()==False:
        n=temp1.pop()
        S.push(n)
    while temp2.isempty()==False:
        k=temp2.pop()
        S.push(k)
    print("R is", R.data)
    print("S is", S.data)
