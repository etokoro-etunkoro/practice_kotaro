import math
def primeJudge(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

prime = []
target = int(input())
for i in range(target + 1):
    if primeJudge(i):
        prime.append(i)
print(prime)
primes = set(prime)
if target in prime:
    print("Yes")
else:
    print("No")