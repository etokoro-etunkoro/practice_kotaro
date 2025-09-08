def hanoi(n, source, destination, via): #引数→ブロック数, 移動元, 移動先, 経由地
    if n > 1:
        hanoi(n-1, source, via, destination)    #帰納的に書く
        print(source + '->' + destination)
        hanoi(n-1, via, destination, source)    
    else:   #hanoi(1)の定義
        print(source + '->' + destination)

n = int(input())
hanoi(n, 'a', 'b', 'c')
