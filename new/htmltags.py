def html_tags(raw_code):
    stk=stack.LimitedStack()
    j=raw_code.find('<')
    if j!=-1:
        k=raw_code.find(' ',j+1)
    if k==-1:
        return False
    tag=raw_code[j+1:k]
    if not tag.startswith('/'):
        stk.stack_push(tag)
    else:
        if stk.isempty():
            return False
        if tag[1:]!=stk.pop():
            return False
    j=raw_code.find('<', k+1)
    return stk.isempty()
