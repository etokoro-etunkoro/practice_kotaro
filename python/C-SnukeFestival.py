def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data) - (i+1)):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data

def binary_left(data, target): #二部探索っぽく,dataのなかでtarget以上がでてくる最小のindexを返す
    bubbleSort(data)
    left = 0
    right = len(data)   #ここはlen(data)-1ではない気がするぞ要確認

    while left < right:

        mid = (left + right) //2

        if data[mid] < target:  #targetはdata[mid]よりでかい→まだ絞り込む
            left = mid + 1        
        else:   #data[mid]がtargetと一致しててもさらに左に進むので、複数あっても最小のindexを探すことができる
            right = mid

    #left = rightになったらそのleftがdata[i]>=targetとなる最大のi
    return left

def binary_right(data, target): #dataのなかでtargetより大きい最小のindexを返す
    bubbleSort(data)
    left = 0
    right = len(data)
    while left < right:
        mid = (left + right) // 2
        if data[mid] <= target: #今回はdata[mid]がtargetと同じだとさらに右にすすむ→つまり複数targetと同じものがあってもdata[i]>targetとなる最小のiを探すことができる
            left = mid + 1
        else:
            right = mid
    
    return left

N = int(input())
A = bubbleSort(list(map(int, input().split())))
B = bubbleSort(list(map(int, input().split())))
C = bubbleSort(list(map(int, input().split())))
counter = 0
for i in range(N):
    J = binary_right(B, A[i])   #J, J+1, ..., N-1の(N-J)個がA[i]より大きい
        #わかんなくなっちゃった
    for j in range(J, N):   
        K = binary_right(C, B[j])
        counter += (N-K)

print(counter)
    
    

