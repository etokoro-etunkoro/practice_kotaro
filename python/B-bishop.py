from math import ceil, floor

W, H = map(int, input().split())
HW = H*W
ans = ceil(HW /2)
if H == 1 or W == 1:
    ans = 1
    print(ans)
else:
    print(ans)