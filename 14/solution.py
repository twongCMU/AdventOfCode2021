#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict

# defaultdict(str)
# defaultdict(int)

data = []


with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

graph = list(data[0])

d = {}
for row in data:
    if "->" in row:
        (a, b) = row.split(" -> ")
        d[a] = b

def iterate_graph(graph):
    i = 0
    # -1 because we're checking 2 elements at a time
    while i < len(graph)-1:
        test = graph[i]+graph[i+1]
        if test in d:
            graph.insert(i+1, d[test])
            i += 2
        else:
            i += 1

    return graph

for j in range(10):
    print(f"round {j}")
    graph = iterate_graph(graph)

dist = {}
for v in graph:
    if v not in dist:
        dist[v] = 0
    dist[v] += 1

values = dist.values()
print(f"{max(values) - min(values)}")
