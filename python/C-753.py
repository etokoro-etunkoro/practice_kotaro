import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())
counter = 0
counter2 = 0
def dfs(n, has3, has5, has7):
    global counter
    if n > N:
        return
    
    if has3 and has5 and has7:
        counter += 1
    
    dfs(n*10 +3, True, has5, has7)
    dfs(n*10 +5, has3, True, has7)
    dfs(n*10 +7, has3, has5, True)

dfs(0, False, False, False)
print(counter)

#7,5,3が一回もでなくてもよかった場合は?
#つまり、7,5,3以外の数字がでてこない場合の数を数えたい

def dfs2(n, has3, has5, has7):  #別にhas3とかいらなくね　って感じ
    global counter2
    if n > N:
        return
    
    if has3 or has5 or has7:
        counter2 += 1
    
    dfs2(n*10 +3, True, has5, has7)
    dfs2(n*10 +5, has3, True, has7)
    dfs2(n*10 +7, has3, has5, True)

dfs2(0, False, False, False)
print(counter2)