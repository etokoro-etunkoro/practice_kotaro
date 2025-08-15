N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = {}
count = 0
for i in range(1, N+1):
    A[i] = list(map(int, input().split()))
    sum = 0
    for j in range(0,M):
        sum += A[i][j-1] * B[j-1]
    sum += C
    if sum > 0:
        count += 1

print(count)