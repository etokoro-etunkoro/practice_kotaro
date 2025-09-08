def bubble_sort(data):
    change = True   #交換の余地をフラグとして管理

    for i in range(len(data)):
        if not change:
            break   #交換の余地がなければbreakする
        change = False #交換の余地がないと仮定

        for j in range(len(data) - (i+1)):
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
                change = True #交換の余地はまだあった
    return data

if __name__ == '__main__':
    Data = list(map(int, input().split()))
    sorted_data = bubble_sort(Data.copy())
    print(f"{Data} → {sorted_data}")