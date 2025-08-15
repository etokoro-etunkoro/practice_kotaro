N = int(input())
X = list(map(int,input().split()))
ans = float('inf')
for P in range(1, max(X) + 1):
    total = 0
    for i in range(0, N):
        total += (X[i] - P)**2
    ans = min(total, ans)
print(ans)