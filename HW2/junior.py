# УРОВЕНЬ JUNIOR
# 6-значный билет считается счастливым,
# если сумма 3 первых цифр равна сумме последних 3 цифр.
# Посчитать, сколько существует счастливых 6-значных билетов.

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


print(getCntLuckyTicketsRandomLen(6))
