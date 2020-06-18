#Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
#Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

#Для начала cделаем функцию для проверки ввода пользователя
def check_param(p1,p2):
        try:
            if float(p1)>0 and int(p2)<0:
                return True
            else:
                return False
        except ValueError:
            return False

#Запрашиваем переменные у пользователя
while True:
    user_x=input("Введите действительное положительное число x: ")
    user_y=input("Введите целое отрицательное число y: ")
    if check_param(p1=user_x, p2=user_y):
        print("Числа - супер! Работаем!")
        break
    else:
        print("Как минимум одно из условий не соблюдается. Попробуйте еще раз")


#Переходим к самой функции возведения в степень
#1 способ
def my_func(x,y):
    return (float(x)**int(y))
#2 способ (без использования **)"""
def my_func2(x,y):
    x=float(x)
    y=abs(int(y))
    res=x
    for z in range(1,y):
        res=res*x
    return 1/res

print (f"Если {user_x} возвести в степень {user_y} первым способом, получится {my_func(x=user_x, y=user_y)}")
print (f"Если {user_x} возвести в степень {user_y} вторым способом, получится {my_func2(x=user_x, y=user_y)}")
