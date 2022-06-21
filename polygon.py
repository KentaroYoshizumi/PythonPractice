#def polygon():
#    N = int(input("type a polygon:"))
#    L1 = int(input("Type a L1:"))
#    L2 = int(input("Type a L2:"))
#    L3 = int(input("Type a L3:"))
#    LN = L1 + L2 + L3
#    if 3 < N &&
#        print("Yes")
#    else:
        print("No")
    
#polygon()

def polygon():
    n = int(input())
    a = list(map(int, input().split()))
    newlist = sorted(a, reverse=True)
    answer = "No"

    if newlist[0] < sum(newlist[1:n]):
        answer = "Yes"
    print(answer)

polygon()
