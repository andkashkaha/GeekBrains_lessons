#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

user_vyruchka=float(input("Сколько вы заработали за год: "))
user_izder=float(input("Сколько вы потратили за год: "))

fin_result=user_vyruchka-user_izder

if fin_result<0:
    print(f"Ваша фирма работает в убыток. Ваш результат: {fin_result:.2f}")
elif fin_result==0:
    print("Ваша фирма работает в ноль")
else:
    print(f"Кажется, дела вашей фирмы идут неплохо. Ваша прибыль: +{fin_result:.2f}")
    print(f"Рентабельньсть выручки: {(fin_result/user_vyruchka):.2f}")
    employee_count=int(input("Сколько сотрудников в вашей фирме: "))
    result_for_person=fin_result/employee_count
    print(f"Прибыль в рассчете на одного сотрудника: {result_for_person:.2f}")

