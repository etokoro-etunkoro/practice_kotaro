#10進数を2進数に変換する。
target = int(input())
result = ""
while target > 0:
    result = str(target%2) + result  #前回のあまりの前に、今回のあまりをくっつける
    target = target // 2 #あまり切り捨てで、２で割る
print(result)