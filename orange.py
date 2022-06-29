class Orange:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        print("Created!")


orange1 = Orange(50, "red")
print(orange1.weight)
print(orange1.color)

orange1.weight = 100
orange1.color = "dark orange"

print(orange1.weight)
print(orange1.color)
