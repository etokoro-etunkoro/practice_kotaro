#N桁のbit表示を列挙する
N = int(input())
print(1<<N)
for i in range(1<<N):
    cond = [0]*N    #格納箇所を用意
    for j in range(N):  #N桁目から順に
        if 1 & (i>>j):
            cond[j] = 1
    print(cond)

#3進数表記だとどうだろうか？
M = int(input())
print(3**M)
for i in range(3**M):
    cond = [0] * M
    for j in range(M):
        if (i // (3**(M-j-1))) % 3 == 2:
            cond[j] = 2
        elif (i // (3**(M-j-1))) % 3 == 1:
            cond[j] = 1
        else:
            cond[j] = 0
    print(cond)