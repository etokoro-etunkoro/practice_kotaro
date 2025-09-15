#ソートする関数をつくる
def bubbleSort(data):
    change = True
    for i in range(len(data)):
        if not change: break

        change = False

        for j in range(len(data) - (i+1)):  #(i)個が確定しているので
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                change = True
    return data

def binarySearch(data, target):
    left = 0
    right = len(data) - 1
    while left < right:
        mid = (left + right) // 2  
        if data[mid] >= target:
            right = mid #target以上の最小値は[left, mid]にある
        elif data[mid] < target:
            left = mid + 1

    return left #ここがtarget以上の最小値

N, Q = map(int, input().split())
A = list(map(int, input().split()))
x = [[] for i in range(Q)]
for i in range(Q):
    x[i] = int(input())

bubbleSort(A)
for i in range(Q):
    print(N - binarySearch(A, x[i]))




