# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

user_name=input('Введите ваше имя: ')
user_year=int(input('Введите год своего рождения: '))
user_temperatute=float(input('Введите вашу температуру (через точку): '))
current_year=2020

age=current_year-user_year
print ('Добрый день, ', user_name)
print ('Ваш возраст: ', age)
print ('Ваша температура: ', user_temperatute)

if  age<60 and 36.0<user_temperatute<37.0:
    print('У вас все хорошо. Не болейте')
elif age>=60 and 36.0<=user_temperatute<37.0:
    print('Кажется, у вас все в продяке, но вы в группе риска. Оставайтесь дома и берегите себя')
elif user_temperatute>=37.0:
    print('У вас один из симптомов COVID-19. Срочно обратитесь к врачу')
elif user_temperatute<36.0:
    print('У вас низкая температура. Берегите себя')
else:
    print('Мы не учли какое-то условие. До свидания')

