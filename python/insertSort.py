#挿入ソート
def insertSort(data):
    for i in range(1, len(data)):
        temporary = data[i] #挿入するデータ
        j = i - 1
        while (j >= 0) and (data[j] > temporary):   #挿入データがソート済みと比較して小さいときは続けて入れ替え
            data[j+1] = data[j] #ひとつ左に移す
            j = j-1 #インクリメント
        data[j+1] = temporary   #挿入データがソート済みと比較して大きいときに、空いた箇所に挿入
    return data

data = list(map(input().split()))
sorted_data = insertSort(data)
print(sorted_data)