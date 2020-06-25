#1.Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
newlist=[]
while True:
    user_str=input("Вводите строку: ")
    if user_str=="":
        break
    newlist.append(user_str+"\n")

doc=open("Task1_2.txt","w", encoding="utf-8")
doc.writelines(newlist)
doc.close()