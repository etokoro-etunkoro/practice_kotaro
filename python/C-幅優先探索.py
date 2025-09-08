from collections import deque

#幅優先探索をつかって迷路を解く

R, C = map(int, input().split())
sy, sx = map(int, input().split())  #スタート地点
gy, gx = map(int, input().split())  #ゴール地点

#配列は0からスタートするので、それぞれの値を-1する必要があるんですね
sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1

c = [[c for c in input()] for _ in range(R)]    #迷路のセルを入力する

visited = [[-1]*C for _ in range(R)]    #初期は-1で訪れていない扱い

def bfs(sy, sx, gy, gx, c, visited):
    visited[sy][sx] = 0 #スタート地点は訪れた！
    Q = deque([])
    Q.append([sy, sx])
    while Q:
        y, x = Q.popleft()  #隣接していて、次に訪れる点
        if [y, x] == [gy, gx]:
            return visited[y][x]    #もうゴールについたので、そこのvisitedが答え

        for i, j in [(0,1), (1,0), (-1, 0), (0, -1)]:   #進み方を変位で表している
            if c[y+i][x+j] == '.' and visited[y+i][x+j] == -1:
                #探索可能かつ未訪問のときは...
                visited[y+i][x+j] = visited[y][x] + 1
                Q.append([y+i][x+j])

print(bfs(sy,sx,gy,gx,c,visited))




