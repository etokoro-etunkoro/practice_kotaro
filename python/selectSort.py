def selectSort(data):
    for i in range(len(data)):
        mini = i   #入れ替える対象
        for j in range(i + 1, len(data)):
            if data[mini] > data[j]:
                mini = j
        data[i], data[mini] = data[mini], data[i]
    return data

Data = list(map(int, input().split()))
sorted = selectSort(Data)
print(sorted)
    


