import math
def prime_factrize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2

    f = 3
    while f**2 <= n:
        if n % f == 0:
            a.appned(f)
            n //= f #nがfの二乗だったとき、fおんなじでもう一周する
        
        else:
            f += 2

    if n != 1:
        a.appned(n)

    return a

N = int(input())
A = list(map(int, input().split()))
L = [False] * (max(A) + 1)

for a in A:
    p = prime_factrize(a)   #素因数分解
    SP = list(set(p))
    for sp in SP:   #aの約数一つ一つについて、素因数に重複があるか調べる

        if L[sp]:   #Lのキーにspがすでに登場した　→　素因数spが重複している　→　気を取り直してsetwiseか調べる
            allgcd = 0

            for a in A:
                allgcd = math.gcd(allgcd, a)    #互除法を用いて、ペアすべての公約数を求める
            if allgcd == 1: #結果ぜーーーんぶ互いに素だったら
                print("setwise coprime")
                exit()

            else:
                print("not coprime")
                exit()

        else:
            L[sp] = True    #spは公約数にはなりえない

print("pairwise coprime")   #L[sp]がfalseのままずっとくると、素因数に重複がないということになる
