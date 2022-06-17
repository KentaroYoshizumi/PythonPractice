#ジャンケンの勝敗判定
#0:グー, 1:チョキ, 2:パー

com = 0
you = 1

if com == 0:
    if you == 0:
        result = "あいこ"
    elif you == 1:
        result = "負け"
    else:
        result = "勝ち"
elif com == 1:
    if you == 0:
        result = "勝ち"
    elif you == 1:
        result = "あいこ"
    else:
        result = "負け"
else:
    if you == 0:
        result = "負け"
    elif you == 1:
        result = "勝ち"
    else:
        result = "あいこ"
        
te = ["グー", "チョキ", "パー"]        
        
print(f"コンピュータ: + {te[com]}")
print(f"あなた: + {te[you]}")
print(f"あなたの{result}")
