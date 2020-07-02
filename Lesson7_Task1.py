# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).

from random import randint

def gen_param(x,y):
    '''Функция генерит списки списков для формирования матрицы с x столбцов и y строк'''
    mat_list=[]
    for z in range(1, y+1):
        mat_list.append([randint(0,100) for z in range(x)]) #в матрице не будем использовать числа больше 100 для удобства восприятия
    return mat_list

class Matrix:
    def __init__(self, list):
        self.list=list

    def __str__(self):
        self.mat_str=""
        for z in self.list:
            self.mat_str=f"{self.mat_str} {str(z).replace(',', '').replace('[', '').replace(']', '')}\n"
        return self.mat_str

    def get_el(self, i, j):
        '''Функция, получающая значение элемета из списка списков j-элемент i-списка'''
        return self.list[i-1][j-1]

    def __add__(self, other):
        fin_list=[] #финальный лист
        for i in range(1,len(self.list)+1):
            prom_list=[] #промежуточный лист
            for j in range(1, len(self.list[i-1])+1):
                prom_list.append(self.get_el(i,j)+other.get_el(i,j))
            fin_list.append(prom_list)
        return Matrix(fin_list)



print("Сейчас мы сгенерим 2 матрицы, а потом сложим их")
try:
    a=int(input("Введите количество столбцов у матриц: "))
    b=int(input("Введите количество строк у матриц: "))
    m1=Matrix(gen_param(a,b))
    m2=Matrix(gen_param(a,b))
    print(f"Матрица1:\n{m1}")
    print(f"Матрица2:\n{m2}")
    print(f"Матрица1 + Матрица2:\n{m1+m2}")
except ValueError:
    print("Надо вводить числа")
