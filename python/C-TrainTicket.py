S = list(map(int, input().strip()))

parts = [0] * 3
total = 0
exam = str()
for i in range(1 << 3):
    total = S[0]
    exam = str(S[0])
    for j in range(3):
        if 1 & (i >> j):
            if i >> j:
                total += S[j + 1]
                exam += '+' + str(S[j+1])
            else:
                total -= S[j]
                exam += '-' + str(S[j+1])

    if total == 7:
        print(exam + "=7")
        break

