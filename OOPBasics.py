class Person:
    # Атрибуты класса
    height = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self, name, age=15):
        self.name = name
        self.age = age


# ~~~~~ Работа с атрибутами ~~~~~
p = Person('Pasha', 30)
print(p.name, p.age)

# Получение списка атрибутов класса
print(Person.__dict__)

# Получение определенного атрибута класса. 400 - дефолтное значение, если такого поля нет
print(getattr(p, 'age', 400))

# Изменение атрибута класса и добавление нового атрибута
p.age = 25
print(p.age)

p.nv = [6, 7, 8, 9, 10]
print(p.nv)

Person.nv = [1, 2, 3, 4, 5]
print(Person.__dict__)

setattr(Person, 'nv', ['a', 'b'])
print(Person.__dict__)

# Удаление атрибута
delattr(Person, 'nv')
print(Person.__dict__)


# ~~~~~ Моносостояние для всех экземпляров ~~~~~
class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


# При изменении атрибута у одного экземпляра, меняется во всех экземплярах
a = Cat()
b = Cat()
print(a.breed, b.breed)
a.breed = 'another'
print(a.breed, b.breed)
