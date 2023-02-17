# Переопределение методов
class Person:

    name = 'Bob'

    def __init__(self):
        print('init Person')  # Унаследуется классом Doctor, если в нем не переопределить поведение

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')


# Помимо методов, подклассу передается и переменные
class Doctor(Person):

    name = 'Ivan'  # Изменили имя. До этого брали из класса Person

    def breathe(self):
        print('Доктор дышит')

