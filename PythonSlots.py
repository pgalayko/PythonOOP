class Point:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Изначально, для класса поинт, мы могли вносить любое количество переменных с любым названием
# __slots__ позволяет конкретно указать, какие переменные нам нужны. Указав при инициализации параметр,
# которого нет в __slots__ - получим ошибку

# При использовании slots, объект будет занимать меньше места, так как будет отсутствовать словарь атрибутов

# При исполнении основных действий над объектами, класс имеющий slots будет выполняться быстрее
class Rectangle:
    __slots__ = '__wight', 'height'

    def __init__(self, a, b):
        self.wight = a  # В этот момент будет вызываться сеттер
        self.height = b

    @property
    def perimetr(self):
        return (self.height + self.wight) * 2

    @property
    def area(self):
        return self.height * self.wight

    @property
    def wight(self):
        return self.__wight

    @wight.setter
    def wight(self, value):
        self.__wight = value
