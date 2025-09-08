S = input()
N = len(S)

#N文字のすきまはN-1個
#ひとつひとつに+を挿入するかしないかで2^(N-1)通りある
res = 0
for i in range(1<<(N-1)):   #0から2*(N-1)-1まで
    tmp = 0
    for j in range(N-1):
        tmp = tmp * 10  #十の位
        tmp = tmp + S[j] - '0' #文字列を整数にする！

        if (i & (1 << j)):  #iのj番目のビットが0ならばプラスが入らない
            res = res + tmp
            tmp = 0
    tmp = tmp * 10
    tmp = tmp + S[-1] - '0'
    res = res + tmp

print(res)

