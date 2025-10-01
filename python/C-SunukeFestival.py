def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data) - (i+1)):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j], data[j+1]

    return data

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a = bubbleSort(a)
b = bubbleSort(b)
c = bubbleSort(c)
ans = 0

def binarySearch_upperBound(data, target):  #data[idx] => keyを満たす最小のidxを返す
        #data[idx] => keyを条件として、okを返す
    ng = -1
    ok = len(data)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if data[mid] < target:
            ng = mid
        elif data[mid] >= target:
            ok = mid
    return ok

def binarySearch_lowerBound(data, target):  #data[idx] < keyを満たす最大のidxを返す
        #data[idx] <= keyを条件として、okを返す
    ng = len(data)
    ok = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if data[mid] < target:
            ok = mid
        elif data[mid] >= target:
            ng = mid
    return ok

#まず一番下から選んでしまいましょう
for i in range(N):
    under = c[i]
    middle__ = binarySearch_lowerBound(b, under) + 1
    #print(middle__)
    for j in range(middle__ ):
        middle = b[j]
        top__ = binarySearch_lowerBound(a, middle)+1
        
        ans += top__

print(ans)
    

    

        
