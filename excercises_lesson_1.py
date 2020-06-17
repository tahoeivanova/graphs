import itertools
import random
import requests
from bs4 import BeautifulSoup
import networkx as nx
from matplotlib import pyplot as plt
import uuid

# 1. Создайте Граф состоящий из Городов миллиоников РФ


# 1. Получим все города-миллионеры
url = 'https://ru.wikipedia.org/wiki/Города-миллионеры_России'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
data = []
table = soup.find('table', class_='wikitable')
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
cities_list = []
cities_population = []
for d in data:
    if d != []:
        cities_list.append(d[1])
        cities_population.append(d[2])
# print(cities, len(cities))

# Получаем словарь из городов
#cities_dict = {i:cities_list[i] for i in range(len(cities_list))}
# print(cities_dict, len(cities_dict))

# Создаем ненаправленный граф количеством в длину словаря
G = nx.Graph()
G.add_nodes_from(cities_list)

# Добавляем атрибут к вершине - pos




x = 0
y = 0
count = 0
for city in cities_list:
    if count%2:
        print(city)
        x+=10000
        y = 1000
    else:
        x += 10000
        y = 0
    G.nodes[city]['pos'] = (x,y)
    count+=1

# Координаты вершин хранятся в словаре
nodes_pos = nx.get_node_attributes(G, 'pos')


# Другой вариант - создать путь графа
# G = nx.path_graph(len(cities_dict))
# Передаем в граф словарь из городов
# G = nx.relabel_nodes(G, cities_dict)

# Добавим атрибуты вершин
for d in data:
    if d != []:
        G.add_node(d[1], population=d[2])

for city in cities_list:
    # print(G.nodes[city]['population'])
    print(G.nodes[city])

# 2. Добавьте ребра между между всеми городами

# создаем пары комбинаций между всеми городами при помощи itertools.combinations
# получаем tuples
cities_combinations = itertools.combinations(cities_list, 2)
cities_combinations_list = list(cities_combinations)
# добавляем tuples в ребра
i = 10
for cities_pair in cities_combinations_list:
    i+=1
    road = random.choice(['auto','railway'])
    # if road == 'railway':
    #     railway_name = f'ж/д №{str(uuid.uuid1())[:3]}'
    # else:
    #     autoroad_name = f'M-{i}'
    road_name = f'трасса №{str(uuid.uuid1())[:3]}'
    G.add_edge(*cities_pair, weight=random.randint(10000,100000))

    G.add_edge(*cities_pair, road=road, road_name=road_name)
    G.add_edge(*cities_pair, road_name=road_name)

arc_road = nx.get_edge_attributes(G, 'road')
arc_road_1 = nx.get_edge_attributes(G, 'road_name')
arc_weigth = nx.get_edge_attributes(G, 'weight')

for attr in arc_road:
    print(attr)
for attr in arc_road_1:
    print(attr)
print('Nodes of graph: ')
print(G.nodes())
print('Edges of graph: ')
print(G.edges())

# Отрисовывем вершины
nx.draw_networkx(G, nodes_pos, node_size=1000)


# Отрисовываем ребра
nx.draw_networkx_edges(G, nodes_pos)


# Подписываем вершины, ребра и веса
nx.draw_networkx_edge_labels(G, nodes_pos, edge_labels=arc_weigth)



# Удалим координатные оси
plt.axis('off')
# nx.draw_networkx(G)
plt.show()

# 3. Задайте ребрам аттрибут ЖД или автодорога
# (если между городами существует прямое ЖД сообщение, то ЖД, иначе автодорога)


# 4. Добавьте ребрам аттрибут с названием маршрута или трассы
