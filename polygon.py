#def polygon():
#    N = int(input("type a polygon:"))
#    L1 = int(input("Type a L1:"))
#    L2 = int(input("Type a L2:"))
#    L3 = int(input("Type a L3:"))
#    LN = L1 + L2 + L3
#    if 3 < N &&
#        print("Yes")
#    else:
#        print("No")
    
#polygon()

def polygon():
    N = int(input("type a number:"))
    L = list(map(int, input("type a number:").split()))
    new_list = sorted(L, reverse=True)
    answer = "No"

    if new_list[0] < sum(new_list[1:N]):
        answer = "Yes"
    print(answer)

polygon()


#整数と配列の入力
N = int(input())
L = list(map(int, input().split()))

#一番長い変を求める
max_L = max(L)

#一番長い辺を除いた合計を求める
L.remove(max_L)
sum_L = sum(L)

if max_L < sum_L:
    print("Yes")
else:
    print("No")
