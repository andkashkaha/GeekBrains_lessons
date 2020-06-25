# 6. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
with open("text_6.txt","r", encoding="utf-8") as doc:
    dict={}
    while True:
        file_list=doc.readline().replace("-", "0").replace("(л)","").replace("(пр)","").replace("(лаб)","").split()
        if file_list==[]:
            break
        dict.update({file_list[0][:-1]: sum(map(int, file_list[1:]))})
print(dict)

