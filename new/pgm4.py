import stack
def reverse_order(S):
    stk3=stack.LimitedStack()
    stk4=stack.LimitedStack()
    while S.isempty()==False:
        w=S.pop()
        stk3.push(w)
    while stk3.isempty()==False:
        y=stk3.pop()
        stk4.push(y)
    while stk4.isempty()==False:
        z=stk4.pop()
        S.push(z)

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
    reverse_order(stk1)
    print("The reverse_order is", stk1.data)
