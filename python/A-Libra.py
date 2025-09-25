a, b, c, d = map(int, input().split())

if a + b == c + d:
    print("balanced")
elif a+ b > c + d:
    print("right")
else:
    print("left")