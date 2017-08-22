import linkedlist
def test_list():
    ls=linkedlist.slist()
    assert(ls.head==None)
    assert(ls.isempty())
    assert(ls.first()==None)
    assert(ls.last()==None)
    ls.add_first(10)
    ls.add_first(30)
    ls.add_tail(20)
    ls.add_tail(50)
    ls.add_tail(35)
    assert(ls.first()==30)
    assert(ls.last()==35)
    assert(ls.ismember(20))
    assert(ls.length()==5)

    print(ls.max())
    print(ls.min())
    ls.add_element(10,49)
    ls.display()
if __name__ == '__main__':
    test_list()
