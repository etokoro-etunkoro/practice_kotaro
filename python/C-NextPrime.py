X = int(input())

def sss(n): #1~nまでの素数判定を与える(エラトステネスのふるい)
    #数iに対して、index: i-1が対応
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = False #1は素数ではない

    for i in range(2,n+1):
        if is_prime(i-1):   #iが素数か?
            j = i * 2   #ならばiの倍数は素数ではないことになるなァ！
        
            while j <= n:
                is_prime[j-1] = False   #iの倍数jは素数ではない
                j += i

    table = [i for i in range(1, n+1) if is_prime[i-1]] #iが素数ならリストに格納する
    return [0] + is_prime, table    #戻り値では先頭に0がくっついているので、インデックス=数となる

is_prime, t = sss(200000)
i = 0
while True:
    if X <= i and is_prime(i):  #iが素数かつXより大きくなって初めて
        print(i)
        exit()  #ループ脱出(実行終了)

    i += 1  #インクリメント