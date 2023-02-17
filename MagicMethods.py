from functools import total_ordering
from time import perf_counter

# Методы __str__, __repr__
class Lion:
    def __init__(self, name):
        self.name = name

    # Отвечает за то, как экземпляр класса будет отображаться внутри системы
    def __repr__(self):
        return f"The object Lion - {self.name}"

    # Отвечает за то, как будет выглядеть класс при вызове str или print
    def __str__(self):
        return f"Lion - {self.name}"


# Методы __len__, __abs__
class Line:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self) # self.__abs__()

    def __abs__(self):
        return abs(self.x2 - self.x1)

# Методы сравнения
# __eq__ - ==
# __ne__ - !=
# __lt__ - <
# __le__ - <=
# __gt__ - >
# __ge__ - >=


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

# При переопределении метода __eq__ сбрасывается метод __hash__
# Неизменяемые типы - hashable, изменяемые - unhashable. Неизменяемые типы могут быть ключами в словаре, изменяемые нет
    def __hash__(self):
        return hash((self.a, self.b))


# Чтобы не реализовывать все методе сравнения, можно использовать декоратор functools.total_ordering.
    # С ним можно определить только __eq и __lt
@total_ordering
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


# Если метод __bool__ не реализован, то при вызове bool() будет использоваться метод __len__.
# При его отсутствии - всегда true
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0


# Методы __call__ позволяет сделать экземпляры класса callable
class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.lenght = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.lenght += len(args)
        print(f'Экземпляр вызывался {self.counter} раз')


# Метод __call__ как декоратор
class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывается функция {self.fn.__name__}")
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f"Функция отработала за {finish - start}")
        return result


@Timer # Равнозначно fact = Timer(fact)
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


# МетодЫ __getitem__, __setitem__, __delitem__
# Добавляют свойства получения, присваивания и удаления значения в коллекции по индексу для атрибута класса
class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, index):
        if 0 <= item < len(self.values):
            return self.values[index]
        else:
            raise IndexError("Index error!")

    # Позволяет менять значения по индексу.
    # Добавляем возможность устанавливать значение по индексу, больше максимального,
    # заполняя отсутствующие значения дефолтными числами
    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0] * diff)
            self.values[key] = value
        else:
            raise IndexError("Index error!")

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError("Index error!")


# Методы __iter__, __next__
class Mark:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.values):
            self.index = 0
            raise StopIteration
        letter = self.values[self.index]
        self.index += 1
        return letter


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

# При такой реализации, без использования встроенной функии iter(), необходимо определить метод __next__
#     def __iter__(self):
#         self.index = 0
#         return self

    # Для итерации оценок
    def __iter__(self):
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


# Как можно сделать класс итерабельным:
# через __getitem__ как итератор
# через __iter__. При существовании __get и __iter - берется __iter
#
#
#
