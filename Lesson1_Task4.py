# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number=input("Введите большое целое положительное число: ")

while int(user_number)<=0:
    print("Ваше число отрицательное или 0. Такое не подходит")
    user_number = input("Введите большое целое положительное число: ")
print('Прекрасное число')

num_count=(len(user_number)) #определеяем кол-во символов строки
num_index=0 #индекс цифры в строке
max_val=0

#print(f"{user_number[num_index]}")
while num_index!=num_count:
    current_val=int(user_number[num_index])
    if current_val>max_val:
        max_val=current_val
    if max_val==9:
        break
    num_index=num_index+1

print(f"Максимальная цифра в вашем числе: {max_val}")
