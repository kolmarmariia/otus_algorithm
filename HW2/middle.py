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


DIRECTORY_PATH = "/Users/kolesnikova/Documents/otus/A01_Счастливые_билеты-1801-057a77/1.Tickets/test."

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


def test(i):
    with open (DIRECTORY_PATH + str(i) +'.in') as f:
        cnt = f.readline()

    print("размерность ", cnt)
    start_time = datetime.now()
    res = getCntLuckyTicketsRandomLen(int(cnt))

    print("затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)

    with open (DIRECTORY_PATH + str(i) +'.out') as f:
        out = f.readline()

    print("out из файла проверки ", int(out))
    print("посчитанный резлуьтат ", int(res))
    if int(res) == int(out):
        print("test ok")
    else:
        print("test not ok")


for i in range(0,10):
    test(i)



