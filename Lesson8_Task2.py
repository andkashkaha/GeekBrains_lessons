# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt=txt

user_a=input("Введите делимое: ")
user_b=input("Введите делитель: ")

try:
    a=int(user_a)
    b=int(user_b)
    if b==0:
        raise MyError("На ноль делить нельзя")
except ValueError:
    print("Вводить надо числа")
except MyError as qwe:
    print(qwe)
else:
    print(f"{a}/{b}={a/b}")
