from collections import deque

N = int(input())
d = [[] for _ in range(N)]
for i in range(N):
    d[i] = int(input())
change = True

"""
for i in range(len(d)):  #sortする   
    if not change: break    #交換の余地がなければbreakして省略
    change = False  #交換の余地がないと仮定
    for j in range(len(d) - (i + 1)):
        if  d[j] > d[j + 1]:
            d[j], d[j+1] = d[j+1], d[j]
            change = True
"""

mochies = set()
for i in range(N):
    mochies.add(d[i])

print(len(mochies))
