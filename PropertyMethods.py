class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        self.__balance = value

    def del_balance(self):
        del self.__balance

    balance = property(fget=get_balance,
                       fset=set_balance,
                       fdel=del_balance)


# Проблематика: есть доступ к важным данным из вне, возможность устанавливать любые значения в атрибуты
# Getter, setter позволяет выполнять действия с приватными атрибутами\

# Указав property, мы можем напрямую получать или присваивать значения приватным атрибутам
# без необходимости вызывать методы get или set

# Используя декоратор @property

class BankAccountDec:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        self.__balance = value

    @balance.deleter
    def balance(self):
        del self.__balance


# ~~~~~ Вычисляемые property ~~~~~
class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

# Позволяет обновлять закэшированное значение area, если изменяется сторона квадрата
    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

# Указывая поле area как property, мы можем использовать метод как атрибут без необходимости вызова
# Добавляя приватный атрибут area, мы избавляемся от необходимости каждый раз пересчитывать этот атрибут.
    @property
    def area(self):
        if self.__area is None:
            self.__area = self.side**2
        return self.__area

