# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
#

class Cell:
    def __init__(self, cnt):
        self.cnt=int(cnt)

    def __add__(self, other):
        return Cell(self.cnt+other.cnt)

    def __sub__(self, other):
        if self.cnt>other.cnt:
            return Cell(self.cnt-other.cnt)
        else:
            return ("Вычитать из меньшей клетки большую нельзя")

    def __mul__(self, other):
        return Cell(self.cnt*other.cnt)

    def __floordiv__(self, other):
        return Cell(self.cnt//other.cnt)

    def __str__(self):
        return str(self.cnt)

    def make_order (self, cl_in_row):
        a="" #Создадим пустую строку
        for z in range(1,self.cnt+1):
            if z in range(cl_in_row, self.cnt+1, cl_in_row):
                a=a+"*\n"
            else:
                a=a+"*"
        return a

c1=Cell(17)
c2=Cell(58)
print(f"Клетка1 {c1} ячеек")
print(f"Клетка2 {c2} ячеек")
print(f"Клетка1+клетка2: {c1+c2}")
print(f"Клетка1-клетка2: {c1-c2}")
print(f"Клетка1*клетка2: {c1*c2}")
print(f"Клетка1//клетка2: {c1//c2}")
print(f"Проверяем метод make_order:\n{c1.make_order(4)}")