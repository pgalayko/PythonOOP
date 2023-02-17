class Doctor:
    def can_cure(self):
        print("I can cure")

    def can_build(self):
        print("I'm a doctor, I can build too")


class Builder:
    def can_build(self):
        print("I'm a builder, i can buld")


class Person(Doctor, Builder):
    pass

# В случае, когда мы у класса Person вызовем метод can_build, будет иметь знаение в каком порядке указано наследование.
# Если первым стоит класс Doctor и у него присутсвует метод can_build, то реализация возьмется оттуда.
print(Person.__mro__)
