# -*- coding: utf-8 -*-
class Person:

    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age

    def say_hello(self, name):
        print('こんにちは、{}さん。私は{}です。'.format(name, self.name))


# インスタンス化
yoshizumi = Person('吉積', '日本', 30)
mike = Person('mike', 'America', 13)

print(mike.say_hello('佐藤'))



#class Orange:
#    def __init__(self, weight, color):
#        self.weight = weight
#        self.color = color
#        print("Created!")
