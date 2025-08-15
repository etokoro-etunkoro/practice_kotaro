N = int(input())
found = False
for x in range((N * 100 // 108),((N + 107) * 100 // 108) + 1):
    if N == x * 108 // 100:
        found = True
        print(x)
        break
if not found:
    print(":(")