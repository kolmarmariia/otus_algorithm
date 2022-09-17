# представления
# неориентированные графы:
# i = 1,2,3
# ориентированные графы:
# i = 4,5
import numpy as np

DIRECTORY_PATH_POWER = "/Users/kolesnikova/Documents/otus/HW17/"

# 3.Матрица инцидентности
# Для хранения используется двумерная матрица размера [V, E],
# в каждом столбце которой записано одно ребро таким образом:
# напротив вершин, инцидентных этому ребру, записаны 1, в остальных случаях 0.

def read_graph_matrix_inc(i):
    with open(DIRECTORY_PATH_POWER + 'graph' + str(i) + '.txt') as f:
        array = [row.strip().split(' ') for row in f]

        cnt_edges = int(array[0][1])
        cnt_nodes = int(array[0][0])

        # задаем ребра
        edges = [[int(s), int(x)] for s, x in array[1:]]

        # задаем массив с нумерацией ребер
        edges_num = [i for i in range(0, cnt_edges)]

        m = np.zeros((cnt_nodes, cnt_edges))
        for k in edges_num:
            # для неориентированного графа
            if i < 4:
                # вычитаем 1 из номера вершины, так как на рисунке вершины нумеруются с 1, а в матрице - с 0
                m[edges[k][0] - 1, k] = 1
                m[edges[k][1] - 1, k] = m[edges[k][1] - 1, k] + 1
            else:
                # для ориентированного графа
                m[edges[k][0] - 1, k] = 1
                m[edges[k][1] - 1, k] = -1

    return m


# Проверка смежности двух заданных вершин а и b
def status_adjacent_nodes(a, b, m):
    # запускаем цикл по ребрам:
    result = "no"
    for k in range(0, len(m[0, :])):
        if ((abs(m[a, k]) + abs(m[b, k])) > 1) and (m[a, k] < 2) and (m[b, k] < 2):
            result = "yes"
            break
    if a == b and m[a, k] == 2:
        result = "yes"
    return result


# Получение списка всех вершин, смежных заданной вершине а.
def list_adjacent_nodes(a, m):
    set_nodes = []
    nodes = len(m[:, 0])
    # выбрали все ребра, где присутсвует вершина a
    d = m[:, m[a, :] != 0]
    # идем циклом по всем узлам и проверяем сумму по всем ребрам , где есть вершина a
    for i in range(nodes):
        if (abs(d[i, :]).sum() > 0) & (i != a):
            set_nodes.append(int(i) + 1)
    # отдельное условие на вершину с замкнутым ребром
    d2 = m[:, m[a, :] == 2].sum()
    if d2 > 1:
        set_nodes.append(int(a) + 1)
    return set_nodes


# Вычисление степени заданной вершины a.
# Степень вершины — количество рёбер графа G, инцидентных вершине x.
def calc_pow_node(a, m):
    set_nodes = list_adjacent_nodes(a, m)
    pow = len(set_nodes)
    #если есть кольцо
    d2 = m[:, m[a, :] == 2].sum()
    if d2 > 1:
        pow = pow + 1
    return pow


for k in range(1, 6):
    print(k)
    m = read_graph_matrix_inc(k)
    print(m)
    nodes = len(m[:, 0])
    for i in range(0, nodes):
        print("for ", i + 1, ":")
        # для примера сравниваю две последовательные вершины
        if i < (nodes - 1):
            print("     is adjacent with", i + 2, ":", status_adjacent_nodes(i, i + 1, m))
        else:
            print("     is adjacent with 1:", status_adjacent_nodes(i, 0, m))
        print("     list of adjacent nodes", list_adjacent_nodes(i, m))
        print("     pow=", calc_pow_node(i, m))
