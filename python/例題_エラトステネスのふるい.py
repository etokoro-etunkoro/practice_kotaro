#エラトステネスのふるい

def furui(N):
    is_prime = [True for _ in range(N)]
    #is_prime[0] ~ is_prime[N-1]までのN個が、1~Nまでの数字が素数か否かに対応

    is_prime[0] = False #1は素数で(はない

    for i in range(2, N):   
        
        #is_prime[1~N-1]まで回す
        if is_prime(i-1):   #iが素数か?をi=2~Nまでジャッジ
            j = i * 2

            while j <= N:
                #ならiの倍数であるjは素数ではない→is_prime[j-1]に対応
                is_prime[j-1] = False
                j += i
        
    prime_table = [i for i in range(1, N+1) if is_prime[i-1]]
    return [0] + is_prime, prime_table  #リスト結合

'''
[false, true, true, false, ...]というリストに[0]をくっつけて
[0, false, true, true, false, ...]という新たなリストにしているんだね
'''

N = int(input())
is_prime = [0]*N

furui(N)

