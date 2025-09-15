H, W = map(int, input().split())
C = [[] *W for _ in range(H)]
ans = [0]*H
for i in range(H):
    C[i] = list(map(str, input().split()))

for i in range(H):
    ans[i] = "".join(C[i])
    for _ in range(2):
        print(ans[i])