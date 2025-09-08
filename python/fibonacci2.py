memo = {1:1, 2:1}
def fibonacci(n):
    if n in memo:   #フィボナッチを入れるリストに既にあったら返す
        return memo[n]
    memo[n] = fibonacci(n-2) + fibonacci(n-1)   #なければつくる
    return memo[n]

n = int(input())
print(fibonacci(n))

#計算していった値をどんどん格納していく
