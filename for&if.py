#指定した配列（リスト）を定義し、それらの要素のうち5以上の数をすべて足し合わせた値を出力してください。
array = [4, 0, 5, -1, 3, 10, 6, -8]
result = 0

for i in array:
    if i >= 5:
        result += i
    

print(result)
