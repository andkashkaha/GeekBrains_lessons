#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from random import randint

class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"{self.name} {self.color} начал движение")

    def stop(self):
        print(f"{self.name} {self.color} остановился")

    def turn(self):
        new_dict = {1: "направо", 2: "налево", 3: "назад"}
        i=randint(1,3)
        print(f"{self.name} {self.color} повернул {new_dict.get(i)}")

    # для всех сделаем ограничние 90км\ч в базовом классе
    def show_speed(self):
        if self.speed<=90:
            print(f"{self.name} {self.color} едет со скоростью {self.speed} км\ч. Скорость в пределах нормы")
        else:
            print(f"{self.name} {self.color} едет со скоростью {self.speed} км\ч. Злостный нарушитель! Штраф ему!")


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f"{self.name} {self.color} едет со скоростью {self.speed} км\ч. Скорость в пределах нормы")
        else:
            print(f"{self.name} {self.color} едет со скоростью {self.speed} км\ч. Злостный нарушитель! Штраф ему!")

class WorkCar(Car):
    def show_speed(self):
        if self.speed<=40:
            print(f"{self.name} {self.color} едет со скоростью {self.speed} км\ч. Скорость в пределах нормы")
        else:
            print(f"{self.name} {self.color} едет со скоростью {self.speed} км\ч. Злостный нарушитель! Штраф ему!")

class SportCar(Car):
    pass

class PoliceCar(Car):
    def show_speed(self):
        print(f"{self.name} {self.color} едет со скоростью {self.speed} км\ч. Но полицейским у нас можно все")


lada=TownCar("Lada Седан", "баклажан", 75)
kamaz=WorkCar("Камаз", "желтый", 39)
porsche=SportCar("Porsche", "красный", 90)
ford=PoliceCar("Ford", "бело-синий", 199, True)

lada.go()
kamaz.go()
porsche.go()
ford.go()
lada.turn()
kamaz.turn()
porsche.turn()
ford.turn()
lada.show_speed()
kamaz.show_speed()
porsche.show_speed()
ford.show_speed()
lada.stop()

