import sys
sys.setrecursionlimit(100000)   #再帰回数の上限を引き上げる

N, M = map(int, input().split())
road = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    road[A].append(B)   #Aから行ける都市リストにBを追加

def dfs(s):
    if goal[s]: return  #既にたどり着いている都市であればreturnする
    goal[s] = True  #未到達だったなら、到達済み(到達可能)として
    for r in road[s]: dfs(r)    #sから行ける都市について再帰処理
    #↑ここがdfsのかなめ
ans = 0

for i in range(1, N+1): #N個の都市のうち、iについて始点とする   
    goal = [False] * (N+1)  #iからsに行くことができるかを管理(ここで始点ごとにリセットが入る)
    dfs(i)
    ans = ans + sum(goal)   #始点iから行くことのできる都市数をansに加える

print(ans)


