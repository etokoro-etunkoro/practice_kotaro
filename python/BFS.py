import sys
input = sys.stdin.readline
n, m = map(int,input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)  #aにbが隣接している
    g[b].append(a)  #bにaが隣接している

from collections import deque

def bfs(u):
    queue = deque([u])
    d = [None] * n #uからの距離(初期化)
    d[u] = 0    #自身との距離は0
    while queue:
        v = queue.popleft() #先頭をpopして、その残りを表示
        for i in g[v]:  #vと隣接している点について
            if d[i] is None:    #uとの距離が初期化のままならば
                d[i] = d[v] + 1 #i-u間の距離は、i-v間距離に+1
                queue.append(i) #見つけた点リストにiを追加
                
    return d

#0からの各点の距離
d = bfs(0)
print(d)