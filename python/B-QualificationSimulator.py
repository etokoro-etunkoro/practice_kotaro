N, A, B = map(int,input().split())
S = str(input())
Acount = 0
Bcount = 0
for i in S:
    if i == "c":
        print("No")
    else: 
        if Acount < A+B:
            if i == "a":
                Acount += 1
                print("Yes")
            else:
                if Bcount < B:
                    Acount += 1
                    Bcount += 1
                    print("Yes")
                else:
                    print("No")
        else:
            print("No")
