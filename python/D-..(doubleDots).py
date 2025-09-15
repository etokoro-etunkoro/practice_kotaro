import sys
N, M = map(int, input().split())
g = [[]*N for _ in range(N)]
prev = [-1 for _ in range(N)]
for i in range(M):  #マップ作製
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    g[A].append(B)
    g[B].append(A)

from collections import deque
prev = [-1] * N #初期化
def bfs(u):
    queue = deque([u])
    prev[u] = u #始点の親は始点自身
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if prev[i] == -1:
                prev[i] = v
                queue.append(i)
                

    return 

bfs(0)
if -1 in prev:
    print("No")


else:
    print("Yes")
    for j in range(1,N):    #prev[2]~[N-1]まで出力させたい
        print(prev[j] + 1)  #さっき-1した分を戻す
