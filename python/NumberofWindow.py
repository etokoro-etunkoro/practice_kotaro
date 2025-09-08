N, Q = map(int, input().split())
A = list(map(int,input().split()))
X = list(map(int,input().split()))

sums = 0
for i in range(Q):
    ans = 0
    sums = 0
    right = 0
    
    for left in range(N):
        
        while right < N and sums + A[right] <= X[i]:
            sums += A[right]
            right += 1  #インクリメント
        #こいつがbreakしたときは、rightはf(left)+1である

        ans += (right - left)

        if (left == right): right += right  #leftがrightに追いついたらrightをインクリメント
        #leftがrightに追いつくことは、ある値が馬鹿でかい点でありうる
        else:
            sums -= A[left] #部分和を使いまわす
    print(ans)

                
                
