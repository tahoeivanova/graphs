from matplotlib import pyplot as plt
import networkx as nx
'''
Graph - реализация простого неориентированного графа.
Дополнительные вершины между двумя узлами игнорируются, возможны узлы соединенные с самим собой
DiGraph - ориентированный граф, добавлены функции и ограничения специфическое для этого типа графов.
MultiGraph - реализация мультиграфов, в таких графах граф, возможно существование пар вершин, которые 
соединены более чем одним ребром (ненаправленным), либо более чем двумя дугами противоположных направлений
MultiDiGraph - соответственно ориентированный мультиграф.
'''
"""
# Создаем простой ненаправленный Граф
G = nx.Graph()
print(G.__class__)


# Создаем простой Направленный Граф
G1 = nx.DiGraph()
print(G1.__class__)


# Добавим одну вершину (текст или int)
G.add_node('a')
# Добавим список вершин
G.add_nodes_from(['b', 'c'])

# print('Nodes of graph: ')
# print(G.nodes())
# print('Edges of graph: ')
# print(G.edges())

# То же самое для направленного графа
# Добавим одну вершину (текст или int)
G1.add_node('a')
# Добавим список вершин
G1.add_nodes_from(['b', 'c'])

# print('Nodes of graph: ')
# print(G1.nodes())
# print('Edges of graph: ')
# print(G1.edges())

# Добавим одно ребро, соединяющее вершины a и b
edge = ('a', 'b') # Указываем a и b как tuple
G.add_edge(*edge)

# Теперь добавим одно ребро, соединяющее вершины a и c
edge = ('a', 'c')
G.add_edge(*edge)

# print('Nodes of graph: ')
# print(G.nodes())
# print('Edges of graph: ')
# print(G.edges())


# направленный граф

# Добавим одно ребро, соединяющее вершины a и b
edge = ('a', 'b') # Указываем a и b как tuple
G1.add_edge(*edge)

# Теперь добавим одно ребро, соединяющее вершины a и c
edge = ('a', 'c')
G1.add_edge(*edge)

# print('Nodes of graph: ')
# print(G1.nodes())
# print('Edges of graph: ')
# print(G1.edges())

# Теперь попробуем нарисовать 2 графа с помощью библиотеки matplotlib

nx.draw_networkx(G)
# plt.show() # display

# направленный граф
nx.draw_networkx(G1)
# plt.show() # display
"""
# Путь
# Linked Array
# Создадим Path Graph - линейно связанный граф из заданных вершин
'''
G = nx.path_graph(4)

print('Nodes of graph: ')
print(G.nodes())
print('Edges of graph: ')
print(G.edges())

nx.draw_networkx(G)
plt.show()
'''
# Создадим Path Graph - линейно связанный граф из заданных вершин

'''
cities = {0:'Toronto', 1:'London',2:'Berlin',3:'New York'}
G = nx.path_graph(4)
G = nx.relabel_nodes(G, cities)

print('Nodes of graph: ')
print(G.nodes())
print('Edges of graph: ')
print(G.edges())

nx.draw_networkx(G)
plt.show()
'''

# Зададим вес ребер
G1 = nx.DiGraph() # Создаем направленный граф

# Добавляем 6 вершин
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)
G1.add_node(5)
G1.add_node(6)

# Добавляем ребра и указываем вес каждому
G1.add_edge(1,2, weight=2.0)
G1.add_edge(1,3)
G1.add_edge(2,3, weight=1.0)
G1.add_edge(2,4, weight=4.0)
G1.add_edge(2,5, weight=2.0)
G1.add_edge(3,5)
G1.add_edge(4,6, weight=2.0)
G1.add_edge(5,4, weight=3.0)
G1.add_edge(5,6, weight=2.0)



print('Nodes of graph: ')
print(G1.nodes())
print('Edges of graph: ')
print(G1.edges())


# присвоим координаты вершинам
G1.nodes[1]['pos'] = (0,0)
G1.nodes[2]['pos'] = (2,2)
G1.nodes[3]['pos'] = (2,-2)
G1.nodes[4]['pos'] = (5,2)
G1.nodes[5]['pos'] = (5,-2)
G1.nodes[6]['pos'] = (7,0)
# Координаты вершин хранятся в словаре

node_pos = nx.get_node_attributes(G1, 'pos')
arc_weigth = nx.get_edge_attributes(G1, 'weight')

# Теперь попробуем добавить атрибуты вершин
G1.add_node(1, time='5pm')
G1.add_nodes_from([3], time='2pm')
print(G1.nodes[1])
G1.nodes[1]['room'] = 714
print()
print(G1.nodes.data())


# Отрисовывем вершины
nx.draw_networkx(G1, node_pos, node_size=450)

# Отрисовываем ребра
nx.draw_networkx_edges(G1, node_pos)

# Подписываем вершины, ребра и веса
nx.draw_networkx_edge_labels(G1, node_pos, edge_labels=arc_weigth)

# Удалим координатные оси
plt.axis('off')

# Выводим
plt.show()

# Уникурсальные графы (Эйлеровые)
# который можно начертить без отрыва карандаша от листа бумаги
G = nx.complete_graph(7)
print(list(nx.eulerian_circuit(G)))
nx.draw_networkx(G)
plt.show()


# Проверить, является ли граф уникурсальным
# print(list(nx.eulerian_circuit(G1))) # networkx.exception.NetworkXError: G is not Eulerian
print(nx.is_eulerian(G1))
print(nx.is_eulerian(nx.DiGraph({0:[3], 1:[2], 2:[3], 3:[0]})))
print(nx.is_eulerian(nx.DiGraph({0:[3], 1:[2], 2:[3], 3:[0, 1]})))





