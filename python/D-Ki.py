N, Q = map(int, input().split())
tree = [[] for _ in range(N)]

for _ in range(N-1):    #N-1個の辺に対してつないでいる辺を設定する
    a, b = map(int, input().split())
    tree[a-1].append(b-1)   #配列は0からなので、-1する必要がある
    tree[b-1].append(a-1)

X = [0]*N   #各頂点がもつカウンタ

for _ in range(Q):
    p, x = map(int, input().split())
    X[p-1] = X[p-1] + x

ans = [0]*N

def dfs(u, parent=None):    #uが子、parentが親
    ans[u] = ans[parent] + X[u] #親の答えに、自身のカウンタを加えて自身の答えとする
    for v in tree[u]:   #自身とつながっている頂点について、
        if v != parent: #それが親でなければ
            dfs(v, u)   #自身がそれの親として再帰する(上から下に)


dfs(0,0)
print(''.join([str(i) for i in ans]))   #各頂点のカウンタを出力
