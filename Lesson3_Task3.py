#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

#Для начала cделаем функцию для проверки ввода пользователя
def check_param(p):
        try:
            float(p)
            return True
        except ValueError:
            return False

#Запрашиваем ввод параметров
while True:
    user_a=input("Введите число a: ")
    user_b=input("Введите число b: ")
    user_c=input("Введите число с: ")
    if check_param(user_a) and check_param(user_b) and check_param(user_c):
        break
    else:
        print("Вы вводите что-то не то. Попробуйте еще раз")

#Сама функция my_func
def my_func(a,b,c):
    new_list=sorted([a,b,c])
    return(new_list[-1]+new_list[-2])

print(f"(Сумма 2х максимальных чисел из {user_a}, {user_b}, {user_c} составляет {my_func(float(user_a), float(user_b), float(user_c))}")