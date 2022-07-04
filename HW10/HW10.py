# УРОВЕНЬ JUNIOR.
# Выполнить все пункты.
# BST1. +3 байта. Создать простейшее двоичное дерево поиска и функции:
import time
from datetime import datetime

import numpy as np


# Создаем класс узла
class Tree:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # ф-ия insert(int x) - вставка элемента

    def insert(self, x):
        # сравниваем вставляемое значеие с родительским элеметом
        if self.data:
            if x < self.data:
                if self.left is None:
                    self.left = Tree(x)
                else:
                    self.left.insert(x)
            elif x > self.data:
                if self.right is None:
                    self.right = Tree(x)
                else:
                    self.right.insert(x)
        else:
            self.data = x

    # bool search(int x) - поиск элемента

    def search(self, x):
        if x == self.data:
            return True

        if x < self.data:
            if self.left == None:
                return False
            return self.left.search(x)

        if self.right == None:
            return False
        return self.right.search(x)

    # void remove(int x) - удаление элемента
    def remove(self, x):
        if self.search(x) == True:
            if self == None:
                return self
            if x < self.data:
                self.left = self.left.remove(x)
                return self
            if x > self.data:
                self.right = self.right.remove(x)
                return self
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.data = min_larger_node.data
            self.right = self.right.remove(min_larger_node.data)
            return self

    # void sort() - вывести все элементы в порядке возрастания
    def sort(self):
        if self.left:
            self.left.sort()
        if self.right:
            self.right.sort()


# BST2 +1 байт. Протестировать.
## Создать два дерева из 1000 случайных элементов и 1000 элементов в порядке возрастания.
arr = np.random.random_integers(0, 1000, 1000)
root = Tree(1)
print(len(arr))
start_time = datetime.now()
for i in arr:
    root.insert(i)
print("затраченное время по добавлению элементов неотcортированных",
      (datetime.now() - start_time).total_seconds() * 1000)
time.sleep(2)
del arr, start_time
# Искать 100 случайных чисел в каждом дереве.
arr2 = np.random.random_integers(0, 1000, 100)
print(len(arr2))
start_time = datetime.now()
for i in arr2:
    root.search(i)
print("затраченное время по поиску 100 случайных чисел", (datetime.now() - start_time).total_seconds() * 1000)
time.sleep(2)
# del arr2, start_time

# Удалить 100 случайных элементов в каждом дереве.
arr3 = np.random.random_integers(0, 1000, 100)
print(len(arr3))
start_time = datetime.now()
for i in arr3:
    root.remove(i)
print("затраченное время по удалению 100 случайных чисел", (datetime.now() - start_time).total_seconds() * 1000)
del arr3, start_time
time.sleep(2)

# Создать дерево из 1000 в порядке возрастания
root2 = Tree(1)
start_time = datetime.now()
for i in range(0, 999):
    root2.insert(i)
print("затраченное время по добавлению элементов отcортированных", (datetime.now() - start_time).total_seconds() * 1000)
time.sleep(2)
del start_time
# Искать 100 случайных чисел в каждом дереве.
arr2 = np.random.random_integers(0, 1000, 100)
print(len(arr2))
start_time = datetime.now()
for i in arr2:
    root2.search(i)
print("затраченное время по поиску 100 случайных чисел в отcортированном дереве",
      (datetime.now() - start_time).total_seconds() * 1000)
time.sleep(2)
del arr2, start_time

# Удалить 100 случайных элементов в каждом дереве.
arr3 = np.random.random_integers(0, 1000, 100)
print(len(arr3))
start_time = datetime.now()
for i in arr3:
    root2.remove(i)
print("затраченное время по удалению 100 случайных чисел в отcортированном дереве",
      (datetime.now() - start_time).total_seconds() * 1000)
del arr3, strt_time
time.sleep(2)

# BST3 +1 байт. Занести результаты тестирования в таблицу.
# Записать время работы каждой задачи для каждого дерева.
# Сформулировать вывод.
