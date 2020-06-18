# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.

def check_latin(k):
    """Проверка на латинские буквы"""
    a=1 #если эта переменная меняется, значит проверка не прошла
    for z in k:
        if z in set(chr(i) for i in range (ord('a'),ord('z')+1)):
            continue
        else:
            a=0
            break

    if a==1:
        return True
    else:
        return False

#Сама функция
def int_func(word):
    """По условию задачи функция может принимать слово только маленькими латинскими буквами"""
    if word.islower() and check_latin(k=word):
        first_lit=word[0].upper()
        another_lit=word[1:]
        result=first_lit+another_lit
        return result
    else:
        return "#Bad arguments"

while True:
    user_word = input("Введите слово латинскими маленькими буквами: ")
    res=int_func(user_word)
    if res=="#Bad arguments":
        print("Условия не соблюдены. Попробуйте еще раз")
    else:
        print(res)
        break

while True:
    user_string=input("Введите много слов через пробел латинскими маленькими буквами: ")
    new_list=[]
    for z in user_string.split():
        res=int_func(z)
        if res=="#Bad arguments":
            print("Условия не соблюдены. Попробуйте еще раз")
            break
        else:
            new_list.append(res)
    print(new_list)
    break

print("Конец")


## Тут очень сыро все. Знаю ,что нужно доработать


