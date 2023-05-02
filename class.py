class MyPoint:
    default_color = 'red'  # class attribute
    # constructor, magic method
    # magic method can be custom per class by defining it here

    def __init__(self, x, y):
        self.x = x  # init variable inside class
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    @classmethod
    def zero(cls):  # cls means class and is a contract
        return MyPoint(0, 0)

    def draw(self):
        print(f"x: {self.x}, y: {self.y}")


point = MyPoint(1, 2)

print(isinstance(point, MyPoint))
print(point.draw())
print(point.default_color)
print(MyPoint.default_color)
point.default_color = 'green'  # instance attribute
print(point.default_color)

#################################################################
point.z = 90  # instance attribute => x,y init by cunstructor and z init here

another = MyPoint.zero()
print(another.draw())
print(another)  # exec __str__ method
print(str(another))  # exec __str__ method

############################## Commpare Object ###################################


class MyPoint:
    def __init__(self, x, y):
        self.x = x  # init variable inside class
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __add__(self, other):
        return MyPoint(self.x + other.x, self.y + other.y)


point1 = MyPoint(1, 2)
point2 = MyPoint(1, 2)
print(point1 == point2)  # without __eq__ it is false
print('add', str(point1 + point2))
