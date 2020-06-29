# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print("\033[34m {}" .format(f"Запуск отрисовки. Так пишет {self.title}"))

class Pencil(Stationery):
    def draw(self):
        print("\033[4m {}" .format(f"Запуск отрисовки. Так пишет {self.title}"))

class Handle(Stationery):
    def draw(self):
        print("\033[7m\033[31m {}" .format(f"Запуск отрисовки. Так пишет {self.title}"))

a=Pen("Ручка")
b=Pencil("Карандаш")
c=Handle("Маркер")
a.draw()
b.draw()
c.draw()
