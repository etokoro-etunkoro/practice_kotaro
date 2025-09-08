import sys
sys.setrecursionlimit(10 ** 9)

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def bubbleSort(data):
    for i in range (len(data)):
        for j in range (len(data) - i -1):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data

A = bubbleSort(A)
B = bubbleSort(B)

def is_ok(X): #Ai*Bi <= Xを満たす個数がKよりも多いか
    counter = 0
    for Ai in A:
        bi = X // Ai
        counter += bisect_right(bi, B)

    return counter >= K

def bisect_right(target, data):
    left = 0
    right = len(data)
    while left < right:
        mid = (left + right) // 2
        if data[mid] <= mid:
            left = mid + 1
        else:  
            right = mid
        
    return left

def meguru_bisect(ng, ok):
    while abs(ok-ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid): 
            ok = mid

        else:
            ng = mid
    return ok   #K以上の個数となるXの最大値

print(meguru_bisect(-1, 10**9))