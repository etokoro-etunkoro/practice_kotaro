#バケットソート
def bucketSort(data):
    bucket = [0] * (max(data)+1)  #データを順番に格納していく箱
    ans = []
    
    for i in data:
        bucket[i] = 1   #データ内にどの数字があるか確認する ← これだとdataに重複している値があったときに、それをカウントできない

    for i in range(min(data), max(data)+1):
        ans.extend([i] * bucket[i])

    return ans

data = list(map(int, input().split()))
print(max(data), min(data))
print(bucketSort(data))

