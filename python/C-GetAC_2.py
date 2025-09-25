N , Q = map(int, input().split())
S = str(input())
l = [0] * Q
r = [0] * Q
T = [0] * N
count = [0] * (N+1)

#累積和作成
for i in range(N):
    count[i] = 0
    T[i] = S[:i]
    t = len(T[i])
    for j in range(t-1):    #最後の文字を除いて、Aを探索
        if T[i][j] == "A":
            if T[i][j+1] =="C": #AのとなりがCか探索
                count[i] += 1   #累積に和をなしていく

print(count)
for i in range(Q):
    l[i], r[i] = map(int, input().split())
    print(count[r[i]] - count[l[i]])
