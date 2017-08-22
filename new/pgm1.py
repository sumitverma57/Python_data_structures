import stack
def test_emptystack():
    stk=stack.LimitedStack()
    assert(stk.isempty())
    assert(stk.length()==0)
def transfer(S,T):
    while S.isempty()==False:
        ls=S.pop()
        T.push(ls)

if __name__ == '__main__':
    test_emptystack()
    stk1=stack.LimitedStack()
    stk1.push(24)
    stk1.push(45)
    stk1.push(67)
    stk1.push('hgfffj')
    stk2=stack.LimitedStack()
    transfer(stk1,stk2)
    print("the new stack is", stk2.data )
