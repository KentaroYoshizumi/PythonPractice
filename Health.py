class Health:
    def __init__(self, name):
        self.name = name

    def judge(self, height):
        if (height >= 160):
            result = '大きいさん'
        else:
            result = '小さいさん'
        return result


name = str(input("名前は？: "))
height = float(input("身長(cm)は？: "))
a001 = Health(name)
result = a001.judge(height)
print("名前: " + a001.name)
print("あなたは: " + result)
