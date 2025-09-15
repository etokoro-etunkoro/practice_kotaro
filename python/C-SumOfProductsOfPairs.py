N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7
sum = [0] * N
res = [0]* N
ans = 0
sum[0] = A[0]
for i in range(1, N):
    sum[i] = sum[i-1] + A[i]

for i in range(1, N):
    res[i-1] = sum[i-1]  
    res[i-1] *= A[i]
    res[i-1] %= mod
    ans += res[i-1]

print(ans % mod)



