# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Реализовать общий подсчет расхода ткани.
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def material_count(self):
        pass

class Coats(Clothes):
    def __init__(self, v):
        self.v=v

    @property
    def material_count(self):
        return (self.v/6.5 + 0.5)

class Suits(Clothes):
    def __init__(self, h):
        self.h=h

    @property
    def material_count(self):
        return (2*self.h + 0.3)


try:
    co_count=int(input("Сколько пальто вы собираетесь сшить: "))
    coats_list = []
    suits_list = []
    if co_count<=0:
        print("Видимо, вам не нужно пальто")
    else:
        for el in range(1,co_count+1):
            coats_list.append(int(input(f"Введите размер {el} пальто: ")))

    su_count=int(input("Сколько костюмов вы собираетесь сшить: "))
    if su_count <= 0:
        print("Видимо, вам не нужны костюмы")
    else:
        for el in range(1, su_count + 1):
            suits_list.append(int(input(f"Введите рост {el} косюма: ")))
except ValueError:
    print("Вводить нужно числа")

#Создаем экземпляры классов, считаем общее количество для каждого
total_coats = 0
total_suits = 0
if len(coats_list)>0:
    for z in coats_list:
        a1=Coats(z)
        total_coats+=a1.material_count
    print(f"На все пальто понадобится ткани: {total_coats}")

if len(suits_list)>0:
    for k in suits_list:
        b1=Suits(k)
        total_suits+=b1.material_count
    print(f"На все костюмы понадобится ткани: {total_suits}")

print(f"Всего понадобится ткани: {total_coats+total_suits}")