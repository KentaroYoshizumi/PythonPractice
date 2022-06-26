#1~9までの整数を出力する
for i in range(1, 10):
  print(i)

#1~10までを合計する

s = 0
for i in range(1,10):
    s += i
print(s)

#文字列を１つずつ取り出す
name = "Ted"
for character in name:
  print(character)

#入れループ
for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)
