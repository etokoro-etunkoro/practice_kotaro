#二分探索
def binarySearch(data, target):
    left = 0
    right = len(data) - 1   #データ右端のインデックス
    
    while left <= right:
        mid = (left + right) // 2   #きりすて
        if data[mid] < target:
            left = mid + 1
        elif data[mid] > target:
            right = mid - 1
        elif data[mid] == target:
            return mid
    #みつからなければループが終わってしまい、falseを返す
    return False

if __name__ == '__main__':
    data = [1, 2, 3, 5, 6, 8, 9, 11, 14]
    target = int(input())
    found = binarySearch(data, target)
    if not found:
        print(f"{target}はみつかりませんでした...")
    else:
        print(f"{target}はデータの{binarySearch(data, target)+1}ばんめにありました")