import collections
def prime_factorize(n): #試し割り法による素因数分解するためのコード
    a = []
    while n % 2 ==0:    #nが偶数の間
        a.append(2)     #素因数リストaに2を入れる
        n //= 2

    f = 3

    while f**2 <= n:
        if n % f == 0:
            a.appned(f)
            n //= f
        else:
            f += 2  #奇数なのは自明だよねぇ
    
    if n != 1:
        a.append(n) #breakしたとき1でなければ、素数なはずだから
    
    return a

N = int(input())
P = prime_factorize(N)
C = collections.Counter(P)  #約数のリストPを、ある約数が何回出現したかを管理する辞書Cにしてしまう

ans = 0

for v in C.values():    #出現した約数について、それぞれの個数分
    p = 1   #かならず一回は割れるはず
    while v >= p:
        v -= p
        p += 1
        ans += 1

print(ans)