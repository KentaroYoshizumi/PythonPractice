#days = 365
#hours = days * 24
#minutes = hours * 60
#seconds = minutes * 60

#print (hours)
#print (minutes)
#print (seconds)

from datetime import date,timedelta
 
# 翌日を求める timedelta
td = timedelta(days=1)
# 基準日を 2020年2月28日とする
d = date(2022,6,21)
# 基準日の翌日を計算して出力　2022-06-22
print(d + td)
