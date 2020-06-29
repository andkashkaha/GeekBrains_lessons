# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": wage*0.5} #про премию ничего в условии не сказано, сделаем ее 50% от оклада

class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход с учетом премии: {self._income.get('wage')+self._income.get('bonus')}")


a=Position("Алексей", "Алексеев", "Менеджер", 146000)
b=Position("Николай", "Николаев", "Начальник Алексея", 212000)
a.get_full_name()
a.get_total_income()
b.get_full_name()
b.get_total_income()
