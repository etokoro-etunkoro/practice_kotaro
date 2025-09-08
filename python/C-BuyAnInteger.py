A, B , X = map(int, input().split())

#めぐる式二分探索で解いていく。
#まず、探索用のフラグを用意する。
def is_ok(arg):
    return A * arg + B*(len(str(arg))) <= X #買えればT, ダメならF

def bisect(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(bisect(0, 10 ** 9 + 1))   #1 ~ 10^9は答えになる可能性があるので、そこを含んで範囲指定
#こうしておけば、たとえ全部買えたとしてもokは10*9で止まってくれる