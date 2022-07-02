n = int(input())
a = [int(input()) for x in range(n)]

flag = True
for ele in a:
    if ele == 0:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
