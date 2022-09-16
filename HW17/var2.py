# представления
# неориентированные графы:
# i = 1,2,3
# ориентированные графы:
# i = 4,5
# 1.Перечисление множеств
# множества вершин и множества рёбер, их соединяющих
import numpy as np

DIRECTORY_PATH_POWER = "/Users/kolesnikova/Documents/otus/HW17/"


# матрица смежности
# Для хранения рёбер используется двумерная матрица размерности [V, V],
# каждый [a, b] элемент которой равен 1, если вершины a и b являются смежными и 0 в противном случае.

def read_graph_matrix(i):
    with open(DIRECTORY_PATH_POWER + 'graph' + str(i) + '.txt') as f:
        array = [row.strip().split(' ') for row in f]

        cnt_edges = int(array[0][1])

        # вершины первые
        nodes_a = [[int(s)] for s, x in array[1:]]
        # вершины вторые
        nodes_b = [[int(x)] for s, x in array[1:]]

        m = np.zeros((cnt_edges + 1, cnt_edges + 1))
        m[nodes_a, nodes_b] = 1
        # для неориентированных графов:
        if i < 4:
            m[nodes_b, nodes_a] = m[nodes_b, nodes_a] + 1
        m = m[1:, 1:]

    return m


# Проверка смежности двух заданных вершин а и b
def status_adjacent_nodes(a, b, m):
    if m[a, b] > 0 or m[b, a] > 0:
        return "yes"
    else:
        return "no"


# Получение списка всех вершин, смежных заданной вершине а.
def list_adjacent_nodes(a, m):
    set_nodes = []
    for i in range(0, len(m)):
        if m[a, i] > 0 or m[i, a] > 0:
            set_nodes.append(int(i) + 1)
    return set_nodes


# Вычисление степени заданной вершины a.
# Степень вершины — количество рёбер графа G, инцидентных вершине x.
def calc_pow_node(a, m):
    return m[a, :].sum() + m[:, a].sum()


for k in range(1, 6):
    print(k)
    m = read_graph_matrix(k)
    print(m)
    nodes = len(m[1, :])
    for i in range(0, nodes):
        print("for ", i + 1, ":")  # добавляем 1 , так как на графе нумерация вершин с 1 начинается
        if i < (nodes - 1):
            # для примера сравниваю две последовательные вершины
            print("     is adjacent with", i + 2, ":", status_adjacent_nodes(i, i + 1, m))
        print("     list of adjacent nodes", list_adjacent_nodes(i, m))
        print("     pow=", calc_pow_node(i, m))
