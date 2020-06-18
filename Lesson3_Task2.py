#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def new_func (name, surname, year, city, email, phone):
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город: {city}, Email: {email}, Телефон: {phone}")

user_name=input("Имя: ")
user_surname=input("Фамилия: ")
user_year=input("Год рождения: ")
user_city=input("Город: ")
user_email=input("Email: ")
user_phone=input("Телефон: ")

new_func(name=user_name, email=user_email, phone=user_phone, surname=user_surname, city=user_city, year=user_year)

