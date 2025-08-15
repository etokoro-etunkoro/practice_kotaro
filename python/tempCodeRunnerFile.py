N, L, R = map(int, input().split())
X = []
Y = []
count = 0
for i in range(1, N+1):
    X[i], Y[i] = map(int, input().split())
    if X[i] <= L and Y[i] >= R:
        count += 1
print(count)