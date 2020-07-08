# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться

class MyError(Exception):
    def __init__(self, txt):
        self.txt=txt

new_list=[]
while True:
    user_inp=input("Введите число, чтобы оно добавилось в список (для выхода нажмите q): ")
    try:
        if user_inp.isdigit():
            new_list.append(int(user_inp))
        else:
            if user_inp.lower() == 'q':
                print(f"Вы нажали q. Программа будет завершена.\nИтоговый список: {new_list}")
                break
            else:
                raise MyError("Так не пойдет. Нам нужны только числа")
                continue
    except MyError as err:
        print(err)
    else:
        print(f"На данный момент список выглядит так: {new_list}")