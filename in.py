print("Bat" in "Bat in the hat.")

#文字列Sの何番目に特定の文字cを含むか
s = input()
c = input()

for i, ele in enumerate(s):
    if ele == c:
        print(i + 1)
