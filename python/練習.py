def insertSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j = j -1
        data[j+1] = data
    return data

def selectSort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[j], data[min_idx] = data[min_idx], data[j]

    return data

from itertools import accumulate
def preFix(data):
    prefix = [0] + list(accumulate(data))
    return prefix

def selectSort(data):
    N = len(data)
    for i in range(N):
        mini = data[i]
        for j in range(i+1, N):
            if data[j] < data[mini]:
                mini = j
        data[j], data[mini] = data[mini], data[j]
    return data


def insertSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

def binarySearch(data, target):
    left, right = 0, len(data)
    while left < right:
        mid = (left + right) //2 
        if data[mid] >= target:
            right = mid
        if data[mid] < target:
            left = mid + 1
    return left