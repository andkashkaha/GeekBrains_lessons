#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#У пользователя необходимо запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [150,85,41,22,12,12,11,4,4,2]
user_num=int(input("Введите натуральное число: "))
list_len=len(my_list)
print(my_list)

while True:
    if user_num<=int(my_list[list_len-1]):
        my_list.insert(list_len, user_num)
        break
    elif user_num>int(my_list[0]):
        my_list.insert(0, user_num)
        break
    else:
        list_len=list_len-1

print(my_list)