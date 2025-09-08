# buy an integerを解く
A, B, X = map(int, input().split())

#0 ~ 10^9 +1の間で二部探索していく
left = 0
right = 10 ^9 +1
def bisect(A, B , X):
    while left < right:
        mid = (left + right) //2
        if mid * A + len(str(mid)) * B <= X:
            left = mid
        else: 
            right = mid
    return left

print(bisect(A, B , X))