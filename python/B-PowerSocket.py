A, B = map(int,input().split())
D = (B-1) % (A-1)
if (D == 0):
    print((B-1) // (A-1))
else:
    print((B-1) // (A-1) + 1)
