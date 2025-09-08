#線形探索
def linearSearch(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i    #dataのインデックスを返す
    return False    #みつからなかった...

if __name__ == "__main__":
    data = list(map(int,input().split()))
    target = int(input())
    found = linearSearch(data, target)
    if not found:
        print(f"{target}はありませんでした...")
    else:
        print(f"{target}はdataの{found + 1}ばんめにありました")