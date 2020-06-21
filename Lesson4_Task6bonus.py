# Объединить задачи 6a и 6b
from itertools import count, cycle

def my_count():
    a=1265 #с какого числа начнем нумерацию
    for el in count(a):
        yield el

def my_cycle():
    my_list = ["Ночь", "Улица", "Фонарь", "Аптека"]
    for value in cycle(my_list):
        yield value

nval1 = my_count()
nval2 = my_cycle()
for z in range(50):
    print(next(nval1), next(nval2))

