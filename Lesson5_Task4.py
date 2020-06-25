#4.Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

new_dict={"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

doc=open("text_4.txt","r", encoding="utf-8")
res=doc.readlines()
new_list=[]
for z in res:
    new_list.append(z.replace((z.split()[0]),new_dict.get(z.split()[0])))

doc2=open("Task4.txt","w", encoding="utf-8")
doc2.writelines(new_list)
doc.close()
doc2.close()