def cmb(W, H):
    R = [[0]*H for _ in range(W)]   #二次元配列の初期化
    for i in range(W):
        for j in range(H):
            
            R[0][j] = R[i][0] = 1

    return R    #関数内でRを定義してしまったので、引数として渡す必要があるんですね

def calc(P, i, j, R):   
    if i == 0 or j == 0: return 1

    R[i][j] = (calc(P, i-1 ,j,R) + calc(P, i, j-1,R)) % P   #再帰処理

    return  R[i][j]



p = 10 ** 9 + 7
W, H = map(int,input().split())
R = cmb(W, H)   #ここで定義する！


print(calc(p, W-1, H-1, R))

