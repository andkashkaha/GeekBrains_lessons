# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_func (a, b):
    try:
        return (a/b)
    except ZeroDivisionError:
        print ("Очень жаль, но на 0 делить нельзя")


while True:
    user_a=input("Введите число a, которое будем делить: ")
    user_b=input("Введите число b, на которое будем делить: ")
    if user_a.isdigit() and user_b.isdigit():
        break
    else:
        print ("Вводить нужно числа. Попробуйте еще разок")

print(f"Результат деления {user_a} на {user_b}: {my_func(int(user_a),int(user_b))}")
