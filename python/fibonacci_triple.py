memo = {1:1, 2:1, 3:1}
def F(n):
    if n in memo:
        return memo[n]
    memo[n] = F(n-3) + F(n-2) + F(n-1)
    return memo[n]

n = int(input())
print(F(n))