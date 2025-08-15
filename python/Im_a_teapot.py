N = int(input())
S = input().strip()
last3 = S[-3:]
if (last3 == "tea"):
    print("Yes")
else:
    print("No")

# print("Yes" if last3 == "tea" else "No")