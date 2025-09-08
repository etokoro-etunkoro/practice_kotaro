def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - (i+1)):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def binarySearch(data, target):
    sortedData = bubble_sort(data)
    left = 0
    right = len(data) -1
    while left <= right:
        mid = (left+right) // 2
        if sortedData[mid] == target:
            return mid, sortedData
        elif sortedData[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return False, -1

if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    found, data_sorted = binarySearch(data, target)
    if not found:
        print(f"{target}はみつかりませんでした")
    else:
        print(f"{data}-->>{data_sorted}")
        print(f"{target}はsorted_dataの{found + 1}ばんめにあるよ")
        