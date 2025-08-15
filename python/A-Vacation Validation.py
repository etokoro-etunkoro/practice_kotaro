N, L, R = map(int,input().split())
S = input()
found = True
for i in range((L-1), R):
    if S[i] != "o":
        found = False
        break
if not found:
    print("No")
else:
    print("Yes")