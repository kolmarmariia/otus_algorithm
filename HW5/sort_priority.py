#реализация очереди с приоритетом
def sortPriority(arr, n, i):
    #находим макс среди корневого, правого и левого дорчернего элемента
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    #меняем местами , сортируем, пока значение корневого элемена не самое большое
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sortPriority(arr, n, largest)
#вставляем элемент
def enqueue(array, newNum):
    size = len(array)
    if size == 0 :
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) -1, -1, -1):
            sortPriority(array, size, i)
#ф-ия удаляет элемент
def deleteNode (array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    array[i] = array[size - 1]
    array.remove(array[size - 1])

    for i in range((len(array) // 2) -1, -1, -1):
        sortPriority(array, len(array), i)

arr =[]
enqueue(arr, 3)
enqueue(arr, 9)
enqueue(arr, 10)
enqueue(arr, 12)
enqueue(arr, 7)

print (str(arr))

deleteNode(arr, 9)

print(str(arr))




