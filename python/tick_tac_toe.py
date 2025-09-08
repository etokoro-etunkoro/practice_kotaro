#３目ならべ
import random

#勝利条件
finish = [0b111000000, 0b000111000, 0b000000111, 0b100100100, 0b010010010, 0b001001001, 0b100010001, 0b001010100]
def check(player):
    for mask in finish:
        if player == mask:
            return True
        
def play(player1, player2):
    if check(player2):
        print([bin(player1), bin(player2)])
        print("win")
        return  
    
    board = player1 | player2
    if board == 0b111111111:
        print([bin(player1), bin(player2)])
        print("time up")
        return #time up
    
    putable_spot = [i for i in range(9) if (board & (1 << i)) ==0]
    put = random.choice(putable_spot)
    play(player2, player1 | (1 << put))

play(0,0b000000111)
