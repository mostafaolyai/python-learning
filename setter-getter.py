class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price  # private var

    def set_price(self, value):
        if value < 0:
            raise ValueError('negative')
        self.__price = value


# p1 = Product(50)
# print(p1.get_price())

# p = Product(-1)
###################################################
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price  # private var

    def set_price(self, value):
        if value < 0:
            raise ValueError('negative')
        self.__price = value

    # price will be a var that we can set get just by price
    price = property(get_price, set_price)


# p1 = Product(50)
# print(p1.price)
# p1.price = -1  # error
###################################################
class Product:
    def __init__(self, price):
        self.price = price

    # because we used property then we should limit access to set and get
    # first way is __ before set and get but there is other way

    @property  # for getter
    # def get_price(self):
    def price(self):
        return self.__price  # private var

    @price.setter
    # def set_price(self, value):
    def price(self, value):
        if value < 0:
            raise ValueError('negative')
        self.__price = value


p1 = Product(50)
print(p1.price)
p1.price = -1  # error
