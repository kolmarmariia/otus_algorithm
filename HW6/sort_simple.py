import random
from datetime import datetime
#УРОВЕНЬ JUNIOR.

#BUB1. +1 байт. Реализовать алгоритм BubbleSort.
def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#INS1. +1 байт. Реализовать алгоритм InsertionSort.
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#SHS1. +1 байт. Реализовать алгоритм ShellSort.
def shellSort(arr):
    interval = len(arr) // 2
    while interval > 0:
        for i in range(interval, len(arr)):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2
    return arr

# Занести в сравнительную таблицу время сортировки случайного массива размером 100, 1000 и 10000 для каждого алгоритма.
arr = random.sample(range(0, 10000), 100)
arr1 = random.sample(range(0, 10000), 1000)
arr2 = random.sample(range(0, 10000), 10000)
start_time = datetime.now()
for i in range(0, 3):
    if i == 0:
        arr = random.sample(range(0, 10000), 100)
    elif i == 1:
       arr = random.sample(range(0, 10000), 1000)
    else:
        arr = random.sample(range(0, 10000), 10000)
    res = bubbleSort(arr)
    print("len", len(arr))
    #print("bubbleSort", res)
    print("1. bubbleSort, затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    start_time = datetime.now()
    res = insertionSort(arr)
    #print("insertionSort", res)
    print("1. insertionSort, затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    start_time = datetime.now()
    res = shellSort(arr)
    #print("shellSort", res)
    print("1. shellSort, затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
