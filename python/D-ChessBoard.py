S = [[0] for _ in range(8)]
for i in range(8):
    S[i] = input()  #下方向
namae = [0] * 8
namae = ["a", "b", "c", "d", "e", "f", "g", "h" ]


koma = False
komaplase = "0"
k = 0
while koma == False:
    for j in range(8):
        if  S[k][j] == "*":
            koma = True
            komaplase =   str(namae[j]) +str(8-k) 
    k += 1

print(komaplase)