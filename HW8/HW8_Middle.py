#УРОВЕНЬ MIDDLE.
import heapq #This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
import os
import random
import shutil

#+1 байт. Написать функцию (N, T) для генерации текстового файла из N строчек, на каждой строке записано случайное число от 1 до T.
def generate_file(n,t, file_name):
    arr = random.sample(range(1, t), n)
    with open(file_name, 'w') as f:
        for x in arr:
            f.write(str(x)+"\n")
    print("Not sorted values are:", arr)

#ES1. +1 байта. Реализовать алгоритм внешеней сортировки ExternalSort первым способом, создание T разных файлов с последующим слиянием.

def read_n_int(file_, numbers_to_read):
    array_ = []

    if numbers_to_read <= 0:
        return array_

    num = file_.readline()
    while (num):
        array_.append(int(num))
        if len(array_) >= numbers_to_read:
            break
        num = file_.readline()

    return array_

def sort_and_write(file_name, array_to_sort):
    array_to_sort.sort()
    with open(file_name, 'w') as f:
        for x in array_to_sort:
            f.write(str(x)+"\n")

def sort_slices(file_name, buffer_size_):
    chunk = 1
    f = open(file_name)

    if os.path.exists('./tmp/'):
        shutil.rmtree('./tmp/')
    os.mkdir('./tmp/')

    read_arr = read_n_int(f, buffer_size_)
    while (len(read_arr) > 0):
        sort_and_write('./tmp/sorted_' + str(chunk), read_arr)
        read_arr = read_n_int(f, buffer_size_)
        chunk = chunk + 1

    f.close()

def min_heap_sort():
    arr = []
    min_heap = []
    heapq.heapify(min_heap)
    open_files = []
    for f in os.listdir('./tmp/'):
        if os.path.isfile('./tmp/' + f):
            file_ = open('./tmp/' + f)
            open_files.append(file_)
            val = file_.readline()
            heapq.heappush(min_heap, (int(val), file_))

    while (len(min_heap) > 0):
        min = heapq.heappop(min_heap)
        arr.append(min[0])
        next_str = min[1].readline()
        if next_str:
            heapq.heappush(min_heap, (int(next_str), min[1]))
        else:
            min[1].close()

    return arr


def external_sort(input_file, buffer_size_=100):
    sort_slices(input_file, buffer_size_)
    print('Sorted values are:', min_heap_sort())

generate_file(15,20, 'out.txt')
external_sort('out.txt')

#ES2. +1 байта. Реализовать алгоритм внешеней сортировки ExternalSort вторым способом, с двумя вспомогательными файлами.
#ES3. +1 байта. Реализовать алгоритм внешеней сортировки ExternalSort третьим способом, при первом проходе в память загружать блоки по 100 чисел, сортировать их любым другим алгоритмом и отправлять на выход, а потом действовать по алгоритму ES2.
#+2 байта. Занести в сравнительную таблицу время сортировки файлов при:
#N = 10^2, 10^3, 10^4, 10^5, 10^6,
#T = 10, N. (всего 10 вариантов сочетания N и T).
