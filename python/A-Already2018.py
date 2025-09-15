S = list(input())   #文字列をリストにする
if S[3] == "8":
    S[3] = "7"      #直接書き換えられないのでリストにしてから
StrS= "".join(S)    #リストを文字列にする
print(StrS)