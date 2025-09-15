from random import  randrange

N = int(input())
def aveCalc(N):
    dice = [0] * N
    dices = 0
    for i in range(N):
        dice[i] = randrange(6) + 1
        dices += dice[i]
    
    ave = dices / N
    return ave

print(aveCalc(N))
dice = [0] * N 
dices = 0

def diceLoop(M):
    count = 0
    dices = 0
    while(N - dices > 1):
        for j in range(1, 7):
            dices += j
            count += 1
    pattern = 6 ** count *(N-dices)
    return pattern





def oddsCalc(N):
    M = int(input())
    dice = [0] * N
    dices = 0
    print(diceLoop(M))
    odds = diceLoop(M) / (6**N) * 100 // 1
    print(odds)


oddsCalc(N)
