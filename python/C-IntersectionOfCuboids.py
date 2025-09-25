'''
a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

#かぶっているかどうかの判定
#XYについて

XOK ,YOK, ZOK = False, False, False
if a > d:
    if (g < a) and (g > d):
        XOK = True
    elif (j < a) and (j > d):
        XOK = True
else:
    if (g > a) and (g < d):
        XOK = True
    elif (j > a) and (j < d):
        XOK = True

if b > e:
    if (h < b) and (h > e):
        YOK = True
    elif (k < b) and (k > e):
        YOK = True
else:
    if (h > b) and (h < e):
        YOK = True
    elif (k > b) and (k < e):
        YOK = True

if c > f:
    if (i<c) and (i>f):
        ZOK = True
    elif (l<c) and (l>f):
        ZOK = True

else:
    if (i>c) and (i<f):
        ZOK = True
    elif (l>c) and (l<f):
        ZOK = True


if XOK and YOK and ZOK:
    XYZOK = True
else:
    XYZOK = False


if (g == a) or (g == d):
    if YOK and ZOK:
        XYZOK = True
    elif YOK or ZOK:
        if h == b or h == e:
            XYZOK = True
        elif i == c or i == f:
            XYZOK = True

if (j == a) or (j == d):
    if YOK and ZOK:
        XYZOK = True
    elif YOK or ZOK:
        if k == b or k == e:
            XYZOK = True
        elif l == c or l == f:
            XYZOK = True

if (h == b) or h == e:
    if XOK and ZOK:
        XYZOK = True
    elif XOK or ZOK:
        if i == c or i == f:
            XYZOK = True
        elif g == a or g == d:
            XYZOK = True

if XYZOK:
    print("Yes")
else:
    print("No")
'''

a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

def judgeKUKAN(a, b, c, d):
    if a >= d or b <= c:
        return False
    else:
        return True
    

XOK = YOK = ZOK = False

XOK = judgeKUKAN(a, d, g, j)
YOK = judgeKUKAN(b, e, h, k)
ZOK = judgeKUKAN(c, f, i, l)

if XOK and YOK and ZOK:
    print("Yes")
else:
    print("No")