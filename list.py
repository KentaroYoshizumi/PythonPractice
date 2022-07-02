l = input().split()

print(int(l[0]) + int(l[1]))


#文字列 S と整数 i が与えられるので、 S の i 文字目を出力してください。
S = str(input())
i = int(input())
new_list = list(S)
print(new_list[i-1])
