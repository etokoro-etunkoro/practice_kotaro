memo = {1:1, 2:1, 3:1}
memo4 = {1:1, 2:1, 3:1, 4:1}

def F(n):
    if n in memo:
        return memo[n]
    memo[n] = F(n-3) + F(n-2) + F(n-1)
    return memo[n]

n = int(input())
print(F(n))

def G(n):
    if n in memo4:
        return memo4[n]
    else:
        memo4[n] = F(n-4) + F(n-3) + F(n-2) + F(n-1)
        return memo4[n] 
    
print(G(n))