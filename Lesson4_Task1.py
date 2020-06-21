# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary_count():
    script_name, hours, stavka, prem = argv
    try:
        return int(hours)*float(stavka)+float(prem)
    except ValueError:
        return "Вы ввели что-то не то"

print(f"Зарплата сотрудника: {salary_count()}")
