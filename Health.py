class Health:

    def __init__(self, name):
        self.name = name

    def judge(self, height):
        if height >= 160:
            result = "大きいさん"
            return result

        else:
            result = "小さいさん"
            return result


name = str(input("名前は？："))
height = float(input("身長(cm)は？："))
user01 = Health(name)
result = user01.judge(height)
print("名前: " + user01.name)
print("あなたは: " + result)
