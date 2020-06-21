# Условие задачи очень трудно для понимания.
# Если правильно понял, то нужно брать число n и выводить все факториалы до него, начиная с 1.
# Тогда так:
from math import factorial

def fact(n_list):
    for z in n_list:
        yield factorial(z)

n=20 # тут произвольное число
fact_val=fact([el for el in range(1,n+1)])
for i in range(1,n+1):
    print(next(fact_val))
