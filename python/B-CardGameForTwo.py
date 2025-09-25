N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    MaxIndex = i
    for j in range(i+1, N):
        if A[j] > A[MaxIndex]:
            MaxIndex = j
    A[MaxIndex], A[i] = A[i], A[MaxIndex]

cards = 0
alex = bob = 0
while N-cards > 1:
    alex += A[cards]
    cards += 1

    bob += A[cards]
    cards += 1

if N-cards == 1:
    alex += A[cards]
    cards += 1

print(alex - bob)