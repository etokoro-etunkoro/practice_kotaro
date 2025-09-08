#ループで全探索
from collections import deque
def allLoopSearch():
    target = int(input())
    n = int(input())
    I = deque()
    J = deque()
    for i in range(n):
        for j in range(n):
            if i+j == 13:
                I.append(i)
                J.append(j)
    
    while I:
        i = I.pop()
        j = J.pop()
        print(i, j)

allLoopSearch()