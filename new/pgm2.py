import stack
def reverse(s,t):
    while s.isempty()==False:
        w=s.pop()
        t.push(w)


if __name__ == '__main__':
    stk1=stack.LimitedStack()
    stk1.push(10)
    stk1.push(20)
    stk1.push(30)
    stk1.push(40)
    stk1.push(50)
    stk1.push(60)
    stk1.push(70)
    stk1.push(80)
    stk1.push(90)
    stk1.push(100)
    stk2=stack.LimitedStack()
    reverse(stk1,stk2)
    print("the reveresed list is", stk2.data)
