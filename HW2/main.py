#Домашнее задание
#Счастливые билеты.
#Цель:
#Решить задачу «Счастливые билеты» и проверить решение по тестам.
#Создать систему тестирования на основе файлов.
#УРОВЕНЬ MIDDLE
#Скачать и распаковать архив A01_Счастливые_билеты.zip
#Прочитать условие задачи \1.Tickets\problem.txt
#Решить задачу в общем случае и протестировать вручную на тестах, которые находятся в архиве.#
from datetime import datetime
start_time = datetime.now()


def getNextArr(prevArr):
    arr = []
    newLen = len(prevArr) + 9  # длина следующего массива будет больше на 9
    for i in range(0, newLen):
        q = 0  # заготовка нового значения
        for j in range(0, 10):  # берем 10 нужных значений
            if (i >= j) & ((i - j) < len(prevArr)):
                q += prevArr[i - j]  # добавляем
        arr.append(q)
    return arr

def getCntLuckyTicketsRandomLen(num):
    # собственно сам счетчик
    arr = [1] * 10  # записываем в первый массив 10 единиц
    for i in range(0, (num - 1)):  # нужное количество раз
        arr = getNextArr(arr)  # строим следующие массивы
    c = [arr[i] * arr[i] for i in range(len(arr))]
    return sum(c)


for i in range(1,11):
    res = getCntLuckyTicketsRandomLen(i)
    print(res)
    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds()*1000)

