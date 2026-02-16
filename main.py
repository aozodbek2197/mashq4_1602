# 16-mashq
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

# 17-mashq
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

# 18-mashq
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

# 19-mashq
class Bird:
    def fly(self):
        print("Flying")

class Eagle(Bird):
    def fly(self):
        print("Eagle uchadi")

class Penguin(Bird):
    def fly(self):
        print("Penguin ucha olmaydi")

# 20-mashq
class Payment:
    def pay(self):
        pass

class Cash(Payment):
    def pay(self):
        print("Naqd to‘lov qilindi")

class Card(Payment):
    def pay(self):
        print("Karta orqali to‘lov qilindi")
