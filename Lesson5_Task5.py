#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randrange

new_list=[]
for z in range(randrange(10,100)):
    new_list.append(str(randrange(1001))+" ")

with open("Task5.txt","w", encoding="utf-8") as doc1:
    doc1.writelines(new_list)

with open("Task5.txt","r", encoding="utf-8") as doc2:
    res= doc2.readline()
    print(res)
    summa=sum(list(map(int, res.split())))
    print(f"Сумма всех чисел в файле: {summa}")
