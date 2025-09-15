#バブルソート
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#選択ソート
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#挿入ソート
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#マージソート
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

#線形探索
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

#二分探索
def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left  # target以上が初めて出る位置 (lower_bound)

#一次元累積和
from itertools import accumulate

arr = [3, 1, 4, 1, 5]
prefix = [0] + list(accumulate(arr))
    #区間和 [l, r) = prefix[r] - prefix[l]

#二次元累積和
def prefix2d(grid):
    H, W = len(grid), len(grid[0])
    S = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            S[i+1][j+1] = grid[i][j] + S[i][j+1] + S[i+1][j] - S[i][j]
    return S

    #区間和 [y1,y2)×[x1,x2)
def rect_sum(S, y1, x1, y2, x2):
    return S[y2][x2] - S[y1][x2] - S[y2][x1] + S[y1][x1]

#フィボナッチ数列(動的計画法)
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    dp = [0]*(n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
