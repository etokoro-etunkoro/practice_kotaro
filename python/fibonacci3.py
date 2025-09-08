def fibonacci(n):
    fib = [1,1]
    for i in range(2,n):
        fib.append(fib[i-2]+fib[i-1])
    return fib[n-1]
n = int(input())
print(fibonacci(n))

import time
start = time.time()
print(fibonacci(n))
process_time = time.time() - start
print(process_time)