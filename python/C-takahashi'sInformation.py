c = [[0] * 3 for i in range(3)]
for i in range(3):
    c[i] = list(map(int, input().split()))

Flag = True
for j in range(2):
    for i in range(2):
        if c[j][i] - c[j][i+1] != c[j+1][i] -c[j+1][i+1]:
            Flag = False

        if c[j+1][i] - c[j][i] != c[j+1][i+1] -c[j][i+1]:  
            Flag = False
        

if Flag:
    print("Yes")
else:
    print("No")