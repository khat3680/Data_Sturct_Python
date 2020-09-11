"""
-------------------------------------------------------
[program 6]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-06"
-------------------------------------------------------
"""

from Graph import Graph
from Edge import Edge
from functions import prims

data_ = (
    (['A', 'B'], 2), (['A', 'C'], 3), (['A', 'D'], 7), (['B', 'C'], 6),
    (['B', 'G'], 4), (['C', 'E'], 1), (['C', 'F'], 8), (['D', 'E'], 5),
    (['E', 'F'], 4), (['F', 'G'], 2)
)


edges = []
for b in data_:
    edge = Edge(b[0],b[1])   
    edges.append(edge)

graph = Graph(edges)
e, t= prims(graph,'A')
for s in e:
    print(s)
print(t)








    