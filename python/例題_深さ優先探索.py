def dfs(n):
    print(n, end=' ')
    for i in tree[n]:
        dfs(i)

m = int(input())    #頂点の数　頂点は0~(m-1)のm個
tree = [[] for i in range(m)]
for i in range(m):
    tree[i] = list(map(int, input().split()))   #ここで頂点より多くの数を入れたらバグる

dfs(0)
