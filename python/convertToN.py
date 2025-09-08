def convert(n, base):
    result = ""
    while n > 0:
        result = str(n%base) + result
        n = n // base
    print(result)

n = int(input())
base = int(input())
convert(n,base)