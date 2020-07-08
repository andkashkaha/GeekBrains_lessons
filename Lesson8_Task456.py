# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.

# 5 и 6 задания не осилил пока:(

class Equipment():
    def __init__(self, firm, model, price, var):
        self.firm=firm
        self.model=model
        self.var=var
        self.price=price

    def __str__(self):
        return str(f"{self.var} {self.firm} {self.model} {self.price}")

class Printer(Equipment):
    def __init__(self, firm, model, price, pr_type, var='Printer'):
        super().__init__(firm, model, price, var)
        self.pr_type=pr_type

    def __str__(self):
        return str(f"{self.var} {self.firm} {self.model} {self.pr_type} {self.price}")


class Scanner(Equipment):
    def __init__(self, firm, model, price, sc_type, var='Scanner'):
        super().__init__(firm, model, price, var)
        self.sc_type=sc_type

    def __str__(self):
        return str(f"{self.var} {self.firm} {self.model} {self.sc_type} {self.price}")


class Xerox(Equipment):
    def __init__(self, firm, model, price, format, var='Xerox'):
        super().__init__(firm, model, price, var)
        self.format=format

    def __str__(self):
        return str(f"{self.var} {self.firm} {self.model} {self.format} {self.price}")



class Warehouse:
    eq_id=0
    eq_dict={}
    def __init__(self, str1):
        self.str1 = str1

    def add_equipment(self):
        eq_id=eq_id+1
        eq_dict[eq_id]=self.str1
        return eq_dict


p1=Printer('LG', 'x100', '154$', 'Struynyi')
p2=Printer('Samsung', 's1823', '168$', 'Laser')
s1=Scanner('LG', 'u48', '121$', 'Planshet')
x1=Xerox('Sony', '121Tq', '244$', 'A3')


print(p1)
print(p2)
print(s1)
print(x1)

d=Warehouse(p1)
print(d.add_equipment())
