from collections import deque

def palyndromer(pword):
    d = deque(pword)
    while len(d) >1: 
        if d[0] == d[-1]:
            d.popleft()
            d.pop()
            ck="Char IS palindrome"
        else:
            ck="NOT palindrome"
            break
    return ck    