N, M, X = map(int(input().split()))
CA = []

for i in range(N):
    CA.append(list(map(int, input().split())))

ans = float('inf')  #答えの初期値を無限大にしておく

for i in range(2**N):   #読む本の組み合わせについてのbit全探索
    money = 0
    U = [0] * M #理解度

    for j in range(N):
        if ((i >> j) & 1):  #右シフトを順番に行うことで最下位のbitを確認
            money += CA[j][0]
            for k in range(M):  #読んだ本の内容についてbit全探索
                U[k] += CA[j][k+1]  #CA[j]の先頭は本の価格なのでいっこずれる
        
    for j in range(M):
        if U[i] < X:    #条件を満たしていなければbreak
            break

    else:   #breakされていなければ条件達成  
        ans = min(ans, money)
#全探索しても価格が無限大  ならば...

if ans == float('inf'):
    print(-1)

else:
    print(ans)
