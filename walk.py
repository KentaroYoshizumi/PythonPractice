#あなたは健康のために、1日1万歩を歩くことを目標にしました。
#入力として、歩いた距離(km)と歩幅(cm)が与えられるので、
#1万歩を歩いているかどうかを判定して結果を出力してください。
d, s = map(float, input().split())

if d / s >= 0.1:
    print("yes")
else:
    print("no")

    
#d = int(input("歩いた距離"))
#
#s = int(input("歩幅"))
#
#if d * 100000 / s > 10000:
#  print("yes")
#else:
#  print("no")
