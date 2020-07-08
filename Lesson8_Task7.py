# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.

class Complex:
    def __init__(self, com_dig):
        #Разберем все возможные случаи. По идее i должно быть вседа, иначе это уже не комплексное число
        self.i=com_dig[-1]
        #1 если кроме i ничего нет:
        if com_dig=="i":
            self.a=0
            self.b=1
        #2 если у нас число -i:
        elif com_dig=="-i":
            self.a=0
            self.b=-1
        #3 если перед i сразу идет +, т.е. b=1:
        elif len(com_dig)>2 and com_dig.find('+i')!=-1:
            self.a=int(com_dig[:com_dig.find('+i')])
            self.b=1
        #4 аналогично, только перед i идет -, т.е. b=-1
        elif len(com_dig)>2 and com_dig.find('-i')!=-1:
            self.a=int(com_dig[:com_dig.find('-i')])
            self.b=-1
        #5 если все числа есть, и между действит. и мнимым стоит +
        elif com_dig.find('+')!=-1:
            self.a=int(com_dig[:com_dig.find('+')])
            self.b=int(com_dig[com_dig.find('+')+1:-1])
        #6 если все числа есть, и между действит. и мнимым стоит +
        elif com_dig.rfind('-') not in (-1, 0):
            self.a = int(com_dig[:com_dig.rfind('-')])
            self.b = int(com_dig[com_dig.rfind('-'):-1])
        #7 если нет действит. числа:
        elif com_dig.rfind('-') in (-1,0) and com_dig.find('+')==-1:
            self.a=0
            self.b=int(com_dig[:-1])

    def __add__(self, other):
        return Complex(f"{self.a+other.a}+{self.b+other.b}{self.i}")

    def __mul__(self, other):
        return Complex(f"{self.a*other.a+self.b*other.b*-1}+{self.a*other.b+self.b*other.a}{self.i}")

    def __str__(self):
        if self.a==0 and self.b==0:
            return str(0)
        elif self.a==0 and self.b==1:
            return self.i
        elif self.a==0 and self.b==-1:
            return f"-{self.i}"
        elif self.a==0 and self.b not in (-1,0,1):
            return f"{self.b}{self.i}"
        elif self.a!=0 and self.b==0:
            return f"{self.a}"
        elif self.a!=0 and self.b==-1:
            return f"{self.a}-{self.i}"
        elif self.a != 0 and self.b==1:
            return f"{self.a}+{self.i}"
        elif self.a != 0 and self.b < -1:
            return f"{str(self.a)}{str(self.b)}{self.i}"
        elif self.a != 0 and self.b > -1:
            return f"{str(self.a)}+{str(self.b)}{self.i}"


c1=Complex("12+11i")
c2=Complex("5-21i")
c3=Complex("-4+8i")
c4=Complex("-9-10i")
c5=Complex("14-i")
c6=Complex("-2+i")
c7=Complex("-7i")
c8=Complex("4i")
c9=Complex("i")
c10=Complex("-12-13i")

print(f"({c1})+({c10})={c1+c10}")
print(f"({c3})+({c4})={c3+c4}")
print(f"({c1})*({c2})={c1*c2}")
print(f"({c4})*({c6})={c4*c6}")
print(f"({c2})*({c5})={c2*c5}")
print(f"({c7})*({c8})={c7*c8}")
print(f"({c7})*({c9})={c7*c9}")