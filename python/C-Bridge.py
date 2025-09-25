#とりあえずグラフをつくって、DFSするかあ
N, M = map(int, input().split())
g = [[]*N for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    g[A].append(B)
    g[B].append(A)
    

from collections import deque
d = [0] * N

def dfs(u):
    Q = deque([u])
    d[u] = 0
    while Q:
        v = Q.popleft()
        for i in g[v]:
            if d[i] == 0:
                d[i] = d[u] + 1
                Q.append(i)

    return d
        
for i in range(M):
    g
