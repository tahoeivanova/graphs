import networkx as nx

# pro
# задача о 7 кенигсбергских мостах

print(nx.is_eulerian(nx.DiGraph({0:[3], 2:[3], 3:[3], 4:[3]})))
