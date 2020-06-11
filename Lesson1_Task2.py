#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time=int(input("Введите время в секундах: "))

all_minutes=user_time//60
seconds=user_time%60
hours=all_minutes//60
minutes=all_minutes%60

print(f"Время в нужном формате: {hours:02}:{minutes:02}:{seconds:02}")

