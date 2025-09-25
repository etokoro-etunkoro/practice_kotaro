H, W, K = map(int, input().split())
c = [0] * H
for i in range(H):
    c[i] = input()

ans = 0

for gyo in range(1 << H):
    black = 0
    for retsu in range(1 << W):
        black = 0
        for i in range(H):  #各行について
            for j in range(W):  #各列について
                #H*Wのマス目ひとつひとつについて走査していることになる
                if (gyo >> i) & 1 == 0 and (retsu >> j) & 1 == 0 and c[i][j] == "#":
                    black += 1
        #print(black)
        if black == K:
            ans += 1

print(ans)