N = int(input())
t = [0] * (N+1)
x = [0] * (N+1) 
y = [0] * (N+1)
t[0], x[0], y[0] = 0, 0, 0
for i in range(1,N+1):
    t[i], x[i], y[i] = map(int, input().split())

possible = True

i = 0

while possible == True and i < N:
    d = abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
    if t[i+1] - t[i] > d:
        if (t[i+1]-t[i]) % 2 == d % 2:  #毎秒x+yの偶奇は切り替わる
            possible = True
        else: possible = False
    else:
        possible = False
    i += 1  #インクリメント

if possible:
    print("Yes")
else:
    print("No")
