# представления
# неориентированные графы:
# i = 1,2,3
# ориентированные графы:
# i = 4,5
# 1.Перечисление множеств
# множества вершин и множества рёбер, их соединяющих

DIRECTORY_PATH_POWER = "/Users/kolesnikova/Documents/otus/HW17/"
i = 1


def read_graph_var1(i):
    with open(DIRECTORY_PATH_POWER + 'graph' + str(i) + '.txt') as f:
        array = [row.strip().split(' ') for row in f]
        # множество рёбер
        edges = [[int(s), int(x)] for s, x in array[1:]]

        # множества вершин
        nodes = {e for l in edges for e in l}
    return nodes, edges


# Проверка смежности двух заданных вершин а и b
def status_adjacent_nodes(a, b, edges):
    if [a, b] in edges or [b, a] in edges:
        return "yes"
    else:
        return "no"


# Получение списка всех вершин, смежных заданной вершине а.
def list_adjacent_nodes(a, edges, nodes):
    set_nodes = []
    for i in nodes:
        if [a, i] in edges or [i, a] in edges:
            set_nodes.append(int(i))
    return set_nodes


# Вычисление степени заданной вершины a.
# Степень вершины — количество рёбер графа G, инцидентных вершине x.
def calc_pow_node(a, edges, nodes):
    set_nodes = list_adjacent_nodes(a, edges, nodes)
    pow = len(set_nodes)
    #если есть кольцо
    if [a, a] in edges:
        pow = pow + 1
    return pow


for k in range(1, 6):
    print(k)
    nodes, edges = read_graph_var1(k)
    print(edges)
    print(nodes)
    for i in nodes:
        print("for ", i, ":")
        # для примера сравниваю две последовательные вершины
        if i < len(nodes):
            print("     is adjacent with", i + 1, ":", status_adjacent_nodes(i, i + 1, edges))
        else:
            print("     is adjacent with 1:", status_adjacent_nodes(i, 0, edges))
        print("     list of adjacent nodes", list_adjacent_nodes(i, edges, nodes))
        print("     pow=", calc_pow_node(i, edges, nodes))
