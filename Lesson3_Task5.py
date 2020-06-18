def sum_input(str):
    """Выполняет сложение введных чисел по следующему алгоритму:

    Делим введенную строку на отдельные элементы.
    В цикле перебираем полученные список:
    - Приводим каждый элемент листа к float.
    - Если ок, добавляем этот элемент к новому списку
    - Если ошибка, игнорируем, переходим к следующему элементу

    Функция будет возвращать кортеж с двумя элементами.
    Первым элементом будет текущая сумма чисел.
    Вторым элементом будет флаг наличия символа закрытия (0 - спецсимвол не был введен, 1 - спецсимвол был введен)
    """
    user_list = str.split()
    new_list = []  # Вводим новый пустой список для добавления в него только чисел
    exit_symbol = "#"

    for z in user_list:
        """Проверка на закрытие"""
        if exit_symbol in z:
            if len(new_list) == 0:
                return (None, 1)
                break
            else:
                return (sum(new_list), 1)
                break
        """Добавляем элемент в список, если это число"""
        try:
            z = float(z)
            new_list.append(z)
        except ValueError:
            continue

    """Добавим еще проверку на случай, если чисел в вводе не оказалось"""
    if len(new_list) == 0:
        return (None, 0)
    else:
        return (sum(new_list), 0)


"""В бесконечном цикле запрашиваем ввод чисел"""
print("Вводите числа через пробел\n", "Элементы, не являющиеся числами, будут игнорироваться\n",
      "Нажмите Enter для рассчета суммы всех введенных чисел\n", "Для выхода введите #")
final_sum = 0  # Переменная для итогового значения
while True:
    user_inp = input("Введите числа: ")
    result = sum_input(user_inp)  # Вызываем нашу суммирующую функцию
    """Проверяем результат на флаг закрытия. Если есть, выводим сообщение и закрываем"""
    if result[1] == 1:
        if result[0] == None:
            print("Был введен спецсимвол #. Программа будет закрыта")
            break
        else:
            final_sum = final_sum + result[0]
            print(
                f"Был введен спецсимвол #. Программа будет закрыта. Сумма всех чисел до ввода спецсимвола # составляет {final_sum}")
            break
    elif result[1] == 0:
        if result[0] == None:
            print("Вы вообще не ввели чисел. Может на этот раз получится?")
        else:
            final_sum = final_sum + result[0]
            print(f"Сумма всех введененных чисел составляет {final_sum}")
    else:
        print("Не знаю, как это вышло, но этот сценарий не был предусмотрен")
