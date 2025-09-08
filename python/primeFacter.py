import math
import collections
def primeFactor(n):
    if n == 1:
        return 1
    
    elif n < 1:
        return 0
    
    elif not isinstance(n, int):
        return -1
    
    else:

        factor = collections.deque()
        for i in (2, n+1):
            if n == 1: break
            else:
                while n % i == 0:
                    factor.append(i)
                    print(n)
                    n = int(n / i)
                    print(i)
                    print(n)
                    
                    
        return factor
    
n = int(input())
print(primeFactor(n))



    