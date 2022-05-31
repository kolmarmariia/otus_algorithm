# УРОВЕНЬ JUNIOR.
# Выполнить все пункты.
# SEL1. +1 байт. Реализовать алгоритм SelectionSort.
import random
from datetime import datetime


def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# HIP1. +1 байт. Реализовать алгоритм HeapSort.
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)
    return arr


arr = [1, 12, 9, 5, 6, 10]
print(selectionSort(arr))
print(heapSort(arr))

# УРОВЕНЬ MIDDLE.
# +3 байта. Занести в сравнительную таблицу время сортировки случайного массива размером
# 10^2, 10^3, 10^4, 10^5, 10^6 для каждого реализованного алгоритма (дольше двух минут можно не ждать).

# Занести в сравнительную таблицу время сортировки случайного массива размером 100, 1000 и 10000 для каждого алгоритма.
for i in range(0, 4):
    if i == 0:
        arr = random.sample(range(0, 100), 100)
    elif i == 1:
        arr = random.sample(range(0, 1000), 1000)
    elif i == 2:
        arr = random.sample(range(0, 10000), 10000)
    elif i == 3:
        arr = random.sample(range(0, 100000), 100000)
    else:
        arr = random.sample(range(0, 1000000), 1000000)
    start_time = datetime.now()
    res = selectionSort(arr)
    print("len", len(arr))
    # print("selectionSort", res)
    print("selectionSort, затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    start_time = datetime.now()
    res = heapSort(arr)
    # print("heapSort", res)
    print("heapSort, затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
