A = {}
A[0] = list(map(int, input().split()))
A[1] = list(map(int, input().split()))
A[2] = list(map(int, input().split()))

N = int(input())
count = False
B = [int(input()) for _ in range(N)]
marked  = set(B)

for i in range(3):
    if A[i][0] in marked:
        if A[i][1] in marked:
            if A[i][2] in marked:
                count  = True

for j in range(3):
    if A[0][j] in marked:
        if A[1][j] in marked:
            if A[2][j] in marked:
                count = True

for i in range(3):
    if not A[i][i] in marked:
        break
else:
    count = True

for i in range(3):
    if not A[i][2-i] in marked:
        break
else:
    count = True

if count:
    print("Yes")
else:
    print("No")