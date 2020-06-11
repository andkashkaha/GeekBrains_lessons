#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num_value=0

while int(num_value)<=0:
    num_value=input('Введите любое целое положительное число N: ')
    if int(num_value)<=0:
        print ("Это число не годится")
    else:
        print("Отличное число")
        break

result=int(num_value)+int(num_value+num_value)+int(num_value+num_value+num_value)
print('Результат N+NN+NNN: ', result)