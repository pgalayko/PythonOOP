# Переопределение методов
class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')


# Помимо методов, подклассу передается и переменные
class Doctor(Person):

    def __init__(self, name, surname, age):
        super.__init__(name, surname)
        self.age = age

