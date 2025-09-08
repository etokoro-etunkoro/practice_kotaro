N, K = map(int,input().split())
S = [[] for _ in range(N)]
for i in range(N):
    S[i] = int(input())

#Sの中に0があれば全てK以下になる
if 0 in S:
    print(0)
    
else:

    right = 0   #leftが0から始まるとき、rightもまた0から始まっている
    total = 1
    ans = 0
    for left in range(N):
        while right < N and total * S[right] <= K:
            total *= S[right]
            right += 1
        #breakしたとき、rightはf(left)より1大きい
        #条件を満たすrightの数はf(left)-left+1だから...
        if ans < (right - left):
            ans = right - left

        if (left == right): #rightが条件を全く満たさず、leftに追いつかれた場合ちょっと逃げる
            right += 1
        else:
            total /= S[left]

    print(ans)
