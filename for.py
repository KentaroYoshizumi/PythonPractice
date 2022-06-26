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

#入れ子ループ
for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

#n回出力
n = int(input())
for i in range(n):
    print("##########")
    print("..........")

#n回整数を出力
n = int(input())
for i in range(n):
    a_n = int(input())
    print(a_n)
