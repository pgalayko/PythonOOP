class BankAccount:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

# К приватным атрибутам можно также обращаться из вне, достаточно добавить _ к названию атрибута
# Указав атрибут как private, мы не можем обращаться к ним напрямую. Что обеспечивает инкапсуляцию


account1 = BankAccount('Bob', 100000, 43224657)

