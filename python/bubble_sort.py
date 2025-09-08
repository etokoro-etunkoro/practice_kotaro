def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

if __name__ == '__main__':
    Data = list(map(int, input().split()))
    sorted_data = bubble_sort(Data.copy())
    print(f"{Data} → {sorted_data}")