# УРОВЕНЬ JUNIOR.
# Выполнить все пункты.
# CS1. +1 байт. Реализовать алгоритм сортировки подсчётом CountingSort.
import numpy as np
import time
from datetime import datetime

def countingSort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    # Выходной массив символов, который будет отсортирован

    output = len(arr) * [0]

    # Массив подсчета для хранения подсчета отдельных символов
    count = range_of_elements * [0]

    # Кол-во встречаемости каждого из элементов
    for i in range(0, len(arr)):
        count[arr[i] - min_element] += 1

    # Меняем позицию символа на -1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Строим выходной массив
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_element] - 1] = arr[i]
        count[arr[i] - min_element] -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

    return output


# RS1. +1 байт. Реализовать алгоритм поразрядной сортировки RadixSort.

# переписываем countingSort с учетом, что надо элементы разделить по разрядам
def countingSortForRadix(arr, rank):
    length = len(arr)
    output = [0] * length
    count = [0] * 10

    # Кол-во встречаемости каждого из элементов
    for i in range(0, length):
        index = arr[i] // rank
        count[index % 10] += 1

    # Накопительная сумма
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = length - 1
    while i >= 0:
        index = arr[i] // rank
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, length):
        arr[i] = output[i]


def radixSort(arr):
    max_element = max(arr)

    rank = 1
    while max_element // rank > 0:
        countingSortForRadix(arr, rank)
        rank *= 10

    return arr


# BS1. +1 байт. Реализовать алгоритм блочной сортировки BucketSort.

def insertionSort(bucket):
    for i in range(1, len(bucket)):
        fix = bucket[i]
        j = i - 1
        while (j >= 0 and fix < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = fix


def bucketSort(arr):
    max_value = max(arr)
    length = len(arr)
    size = max_value / length

    # Create n empty buckets where n is equal to the length of the input list
    buckets = []
    for x in range(length):
        buckets.append([])

        # распределяем элементы по бакетам
    for i in range(length):
        j = int(arr[i] / size)
        if j != length:
            buckets[j].append(arr[i])
        else:
            buckets[length - 1].append(arr[i])

    # Сортируем элементы внутри бакетов
    for k in range(length):
        insertionSort(buckets[k])

    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(length):
        final_output = final_output + buckets[x]
    return final_output

# +2 байта. Занести в сравнительную таблицу время сортировки
# случайного массива размером 10^2, 10^3, 10^4, 10^5, 10^6 из чисел от 0 до 999.
# для каждого реализованного алгоритма, timeout 2 минуты.
for i in range(0, 4):
    if i == 0:
        arr = np.random.random_integers(0, 999, 100)
    elif i == 1:
        arr = np.random.random_integers(0, 999, 1000)
    elif i == 2:
        arr = np.random.random_integers(0, 999, 10000)
    elif i == 3:
        arr = np.random.random_integers(0, 999, 100000)
    else:
        arr = np.random.random_integers(0, 999,  1000000)
    time.sleep(2)
    start_time = datetime.now()
    print(len(arr))
    countingSort(arr)
    print("1. countingSort, затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    time.sleep(2)
    start_time = datetime.now()
    radixSort(arr)
    print("2. radixSort, затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    time.sleep(2)
    start_time = datetime.now()
    bucketSort(arr)
    print("3. radixSort, затраченное время, миллисекунды ", (datetime.now() - start_time).total_seconds() * 1000)
    time.sleep(2)
