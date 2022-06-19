# УРОВЕНЬ JUNIOR.
# Выполнить все пункты.
# QS1. +1 байт. Реализовать алгоритм быстрой сортировки QuickSort.

# задаем ф-ию для разделения массива
import random


def split(arr, l, r):
    pivot = arr[l]
    low = l + 1
    high = r
    while True:
        # Элементы, меньшие, чем ось, перемещаются влево от оси, а элементы, большие, чем ось, – вправо.
        # также нужно убедиться, что мы не ушли за границу куска массива, так как это
        # означает, что мы уже переместили все элементы на правильную сторону от оси
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1

        # Мы либо нашли значения как для максимума, так и для минимума, которые не соответствуют порядку
        # или low выше high, в этом случае выходим из цикла
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[l], arr[high] = arr[high], arr[l]

    return high


# ф-ия сортировки
def quick_sort(arr, l, r):
    if l >= r:
        return
    m = split(arr, l, r)
    quick_sort(arr, l, m - 1)
    quick_sort(arr, m + 1, r)


arr = random.sample(range(0, 100), 100)
print("было:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("стало:", arr)


# MS2. +1 байт. Реализовать алгоритм сортировки слиянием MergeSort.
# +2 байта. Занести в сравнительную таблицу время сортировки
# случайного массива размером 10^2, 10^3, 10^4, 10^5, 10^6
# для каждого реализованного алгоритма, timeout 2 минуты.
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        # рекурсивный вызов обоих частей
        mergeSort(l)
        mergeSort(r)
        # задаем два итератора для обхода двух частей массива
        i = 0
        j = 0
        # задаем итератор для основного списка
        k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                # будет использовано значение из левой половины
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


arr = random.sample(range(0, 100), 100)
print("было:", arr)
mergeSort(arr)
print("стало:", arr)
