#7. Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

file_list=[]
new_dict={}
with open("text_7.txt","r", encoding="utf-8") as doc:
    while True:
        file_list=doc.readline().split()
        if file_list == []:
            break
        new_dict.update({file_list[0]: int(file_list[2])-int(file_list[3])})


avg_list=[int(el) for el in new_dict.values() if el>=0]
final_list=[new_dict, {"average_profit": sum(avg_list)/len(avg_list)}]
print(final_list)


with open("json_file.json", "w", encoding="utf-8") as json_file:
    json.dump(final_list, json_file, ensure_ascii=False, indent=3)
