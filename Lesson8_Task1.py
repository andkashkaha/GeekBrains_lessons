# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

class Date:
    def __init__(self, dat):
        self.dat=dat

    @classmethod
    def get_date_int(cls, dat):
        dd, mm, yyyy = map(int, dat.split('-'))
        return cls([dd, mm, yyyy]).dat

    @staticmethod
    def check_date(dat):
        dd, mm, yyyy = map(int, dat.split('-'))
        return 1 <=dd<= 31 and 1<=mm<= 12 and 0000<= yyyy<= 3000

print(Date.get_date_int('15-02-1748'))
print(Date.check_date('15-02-1748'))
