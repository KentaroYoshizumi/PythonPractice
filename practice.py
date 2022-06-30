print("Hello,world")

print(1+1)
print(1-1)
print(2*2)
print(10/2)
print(5 % 3)

# 変数
seito = "Hello, world!"
print(seito)

login_id = "seito2022"
print(login_id)

int = 2022


for i in range(10):
    print("tsujimura")

if int == 5:
    print("Yes!")
else:
    print("No!")


def seito():
    seito_status = 10
    if(seito_status < 100):
        print("under 100!")


seito()
print(type(int))

with open('./class.py', 'r') as file:
    print(file.mode)
