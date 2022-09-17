# представления
# неориентированные графы:
# i = 1,2,3
# ориентированные графы:
# i = 4,5
import numpy as np

DIRECTORY_PATH_POWER = "/Users/kolesnikova/Documents/otus/HW17/"


# 5.Векторы смежности
# Для записи вектора смежности используется двумерная матрица размером [V, S],
# где S - максимальная степень вершины в графе.
# В каждой строчке a записаны номера вершин, смежных с а,
# после чего записаны нули (несуществующие номера вершин).

# не поняла, в чем разница неориентированных графов и ориентированных графов в этом случае

def read_graph(i):
    with open(DIRECTORY_PATH_POWER + 'graph' + str(i) + '.txt') as f:
        array = [row.strip().split(' ') for row in f]

        nodes = [[int(s), int(x)] for s, x in array[1:]]
        cnt_nodes = int(array[0][0])

        # считаем максимальную степень вершин (как-то не очень оптимально, но не знаю как лучше):
        nodes_pair = [item for sublist in nodes for item in sublist]
        max_pow = max([nodes_pair.count(i) for i in set(nodes_pair)])

        m = np.zeros((cnt_nodes, max_pow))
        # идем циклом по вершинам:
        for i in range(1, cnt_nodes + 1):
            # выбираем вершины где справа наша вершина
            nodes_x = [x[0] for x in nodes if x[1] == i]
            # выбираем вершины где слева наша вершина
            nodes_y = [x[1] for x in nodes if x[0] == i]
            k = 0
            for p in set(nodes_x + nodes_y):
                m[i - 1, k] = int(p)
                k = k + 1
        return m


# Проверка смежности двух заданных вершин а и b
def status_adjacent_nodes(a, b, m):
    if b in m[a - 1, :] or a in m[b - 1, :]:
        return "yes"
    else:
        return "no"


# Получение списка всех вершин, смежных заданной вершине а.
def list_adjacent_nodes(a, m):
    return [int(x) for x in m[a - 1, :] if x > 0]


# Вычисление степени заданной вершины a.
# Степень вершины — количество рёбер графа G, инцидентных вершине x.
def calc_pow_node(a, m):
    nodes_pair = [x for x in m[a - 1, :] if x > 0]
    pow = len(nodes_pair)
    if a in m[a - 1, :]:
        pow = pow + 1
    return pow


for k in range(1, 6):
    print(k)
    m = read_graph(k)
    print(m)
    nodes_cnt = len(m)
    for i in range(1, nodes_cnt + 1):
        print("for ", i, ":")
        # для примера сравниваю две последовательные вершины
        if i < nodes_cnt:
            print("     is adjacent with", i + 1, ":", status_adjacent_nodes(i, i + 1, m))
        else:
            print("     is adjacent with 1:", status_adjacent_nodes(i, 1, m))
        print("     list of adjacent nodes", list_adjacent_nodes(i, m))
        print("     pow=", calc_pow_node(i, m))
