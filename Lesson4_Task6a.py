# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,

from itertools import count
from sys import argv

def my_count():
    script_name, a, b = argv
    try:
        if int(a)>=int(b):
            print("По условиям задачи, второе число должно быть больше первого")
        for el in count(int(a)):
            if el>int(b):
                break
            else:
                print(el)
    except ValueError:
        print("Вводить надо целые числа")

my_count()