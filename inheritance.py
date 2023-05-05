class Animal:
    def __init__(self):
        self.age = 35

    def eat(self):
        print('eat from parent')


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 350

    def walk(self):
        print('walk animal')


# class Zebra(Animal, Cat): you should change place of both because cat extended animal class, wierd
class Zebra(Cat, Animal):
    pass


class Dog(Animal):
    def eat(self):
        print('eat from dog')


cat = Cat()
cat.eat()
print(cat.age)
print(cat.weight)

dog = Dog()
dog.eat()
print(dog.age)
