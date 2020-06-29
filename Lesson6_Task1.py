# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
import time

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color=="Красный":
            print("\033[31m {}" .format(self.__color))
            time.sleep(7)
        elif self.__color=="Желтый":
            print("\033[33m {}" .format(self.__color))
            time.sleep(2)
        elif self.__color=="Зеленый":
            print("\033[32m {}" .format(self.__color))
            time.sleep(6)


red = TrafficLight("Красный")
yellow = TrafficLight("Желтый")
green = TrafficLight("Зеленый")

while True:
    red.running()
    yellow.running()
    green.running()
    yellow.running()
