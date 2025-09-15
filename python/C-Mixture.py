from collections import deque
ans = []
T = int(input())    #テストケースの数
for _ in range(T):
    N = int(input())
    S = "0" + input()   #状態0が含まれていないので、頭に0を足してやる
    G = [[] for _ in range(2**N)]
    
    for i in range(2**N):
        if S[i] == "1": continue    #状態iはそもそも危険なのでとばす
        for bit in range(N):
            if i & (1 << bit) == 0:  #iのbit桁目が0か?
                next = i | (1 << bit)   #iのbit桁目だけ0→1にしたやつ
                if S[next] == "0":  #次の頂点が安全なら
                    G[i].append(next)   #頂点iから行けるところキューに入れる
    que = deque([0])
    seen = [None for _ in range(2**N)]
    seen[0] = 0
    while (que):
        v = que.popleft()
        for v2 in G[v]: #vと隣接している点v2について
            if seen[v2] != None: continue   #もしv2に訪れていたなら、とばす
            seen[v2] = seen[v] + 1
            que.append(v2)
    if seen[2**N-1]:
        ans.append("Yes")
    else:
        ans.append("No")
print(ans)


