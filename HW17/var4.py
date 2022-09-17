# представления
# неориентированные графы:
# i = 1,2,3
# ориентированные графы:
# i = 4,5

DIRECTORY_PATH_POWER = "/Users/kolesnikova/Documents/otus/HW17/"

# 4.Перечень рёбер

def read_graph_edges_list(i):
    with open(DIRECTORY_PATH_POWER + 'graph' + str(i) + '.txt') as f:
        array = [row.strip().split(' ') for row in f]

        # задаем ребра и сразу их номера
        edges = [[int(s), int(x)] for s, x in array[1:]]
        edges2 = [[item, index] for index, item in enumerate(edges)]

    return edges2


# Проверка смежности двух заданных вершин а и b
def status_adjacent_nodes(a, b, m):
    nodes_pair = [p[0] for p in m]
    if [a, b] in nodes_pair or [b, a] in nodes_pair:
        return "yes"
    else:
        return "no"


# Получение списка всех вершин, смежных заданной вершине а.
def list_adjacent_nodes(a, m):
    # получаем пары для нашей вершины
    nodes_pair = [p[0] for p in m if a in p[0]]
    # делаем из пар список с исключениями дублей
    # удаляем из списка нашу вершину
    nodes_pair_for_a = set([item for sublist in nodes_pair for item in sublist if item != a])
    # отдельно рассматриваем случай когда вершина смежная сама себе
    if [a, a] in nodes_pair:
        nodes_pair_for_a.add(a)
    return list(nodes_pair_for_a)


# Вычисление степени заданной вершины a.
# Степень вершины — количество рёбер графа G, инцидентных вершине x.
def calc_pow_node(a, m):
    set_nodes = list_adjacent_nodes(a, m)
    pow = len(set_nodes)
    #если есть кольцо
    nodes_pair = [p[0] for p in m if a in p[0]]
    if [a, a] in nodes_pair:
        pow = pow + 1
    return pow

for k in range(1, 6):
    print(k)
    m = read_graph_edges_list(k)
    print(m)
    nodes_cnt = max(max([p[0][0] for p in m]), max(([p[0][1] for p in m]))) + 1
    for i in range(1, nodes_cnt):
        print("for ", i, ":")
        # для примера сравниваю две последовательные вершины
        if i < (nodes_cnt - 1):
            print("     is adjacent with", i + 1, ":", status_adjacent_nodes(i, i + 1, m))
        else:
            print("     is adjacent with 1:", status_adjacent_nodes(i, 1, m))
        print("     list of adjacent nodes", list_adjacent_nodes(i, m))
        print("     pow=", calc_pow_node(i, m))
