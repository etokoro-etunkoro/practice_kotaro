'''

N, D, P = map(int, input().split())
F = list(map(int, input().split()))

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort(F)

kijun = N // D + 1  #ここまで買うか調べる
summ = [0] * N
summ[0] = F[0]
for i in range(1, N):
    summ[i] = summ[i-1] + F[i]

kaubeki = 0
for i in range(kijun):
    if  summ[D * i - 1]- summ[D* (i-1) -1] < P*i:
        
        break
    else:
        kaubeki += 1

print(kaubeki)
if kaubeki == 0:
    ans = summ[N-1]
elif kaubeki*D >= N:
    ans = P*kaubeki
else:
    ans = P * kaubeki + summ[N-1] - summ[D*kaubeki - 1]
print(kaubeki, summ)
print(ans)
'''

N, D, P = map(int, input().split())
F = list(map(int, input().split()))

def selection_sort(arr):    #Fを昇順に並べ替えるため
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr
    
F = selection_sort(F)   #降順に並べ替えた
#累積和作る




# DP >= Fの合計　となるほど買わなくていいい
setMax = 
