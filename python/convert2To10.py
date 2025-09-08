def convert2to10(n):
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * (2**(len(n)-(i+1)))

    print(result)

n = str(input())
convert2to10(n)
print(int(n, 2)) #int(文字)が10進数にする関数