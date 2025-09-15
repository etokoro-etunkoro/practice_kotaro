N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0
ans = 0
for i in range(0,N):
    for j in range(i+1):
        sum += A[j]
    for j in range(i, N):
        sum += B[j]

    ans = max(ans, sum)
    sum = 0

print(ans)