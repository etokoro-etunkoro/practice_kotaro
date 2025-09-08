import collections
N, M = map(int, input().split())
S = [[] for _ in range(M)]
for i in range(M):  #電球について
    K = list(map(int, input().split()))
    k = K[0]
    S[i] = []*M
    for j in range(1, k+1):
        s = K[j]
        s = s -1
        S[i].append(s)  #要求するスイッチのon/offのならび
    
P = list(map(int, input().split()))
for i in range(M):
    print(S[i])
ans = 0

for mask in range(1<<N):    #0から2^N-1まで、スイッチすべてのon/offの組み合わせを走査
    ok = 0

    for m in range(M):
        count = 0

        for s in S[m]:
            if mask & (1 << s): #maskのs桁目が1なら
                count = count + 1   #onのスイッチを数える

        if count % 2 == P[m]:
            ok = ok + 1
        
    if ok == M:
        ans = ans+1

print(ans)
