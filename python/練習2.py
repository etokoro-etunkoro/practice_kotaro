#セレクトソート
def selectSort(data):
    n = len(data)
    for i in range(n):
        minimum = i
        for j in range(1, n):
            if data[j] < data[minimum]:
                minimum = j
        data[i], data[minimum] = data[minimum], data[i]

    return data



#挿入ソート
def insertSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j = j - 1
        data[j + 1] = key
    return data

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]