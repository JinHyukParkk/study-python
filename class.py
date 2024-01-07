# python 으로 class 만들어서 테스트해보기

class Person:

    # 생성자
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print("hello my name is " + self.name)

    # toString
    def __str__(self):
        return "hyuk is " + str(self.age) + " years old and lives in " + self.address


hyuk = Person("hyuk", 27, "seoul")
hyuk.greeting()
print(hyuk)