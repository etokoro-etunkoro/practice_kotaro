root = 10**9 +7
N = int(input())

answers = [] * (N)
ans = 1

for i in range(1,N+1):
    print(i)
    ans = ans * (i) % root
    answers.append(ans)
print(answers)
print(answers.pop(-1))  #配列最後の値を取得して出力
