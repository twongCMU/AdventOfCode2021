#!/usr/bin/python3

import math
import numpy as np
import re


data = []


with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

graph = {}
# -1 because we're checking 2 elements at a time
letters = list(data[0])
orig_ends = [letters[0], letters[-1]]

for i in range(len(data[0])-1):
    test = letters[i]+letters[i+1]
    if test not in graph:
        graph[test] = 0
    graph[test] += 1

count = 0
for k,v  in graph.items():
    count += v
print(f"Start: expected {len(data[0])} computed {count}")

d = {}
for row in data:
    if "->" in row:
        (a, b) = row.split(" -> ")
        d[a] = b


def iterate_graph(graph):
    #new_graph = graph.copy()
    new_graph = {}
    for k, v in graph.items():
        # if no mapping, copy straight into new graph
        if k not in d:
            if k not in new_graph:
                new_graph[k] = 0
            new_graph[k] += 1

        else:
            # if there is a mapping ac->abc so insert ab and bc
            letters = list(k)
            first = letters[0] + d[k]
            second = d[k] + letters[1]

            if first not in new_graph:
                new_graph[first] = 0
            new_graph[first] += v
            if second not in new_graph:
                new_graph[second] = 0
            new_graph[second] += v
            """
            if first == "BB":
                print(f"From {k}, saving BB first")
            if second == "BB":
                print(f"From {k}, saving BB second")
            """
    return new_graph



for j in range(40):
    print(f"round {j+1}")
    graph = iterate_graph(graph)

    # count letters
    dist = {}
    for k,v in graph.items():

        for a in list(k):
            if a not in dist:
                dist[a] = 0
            dist[a] += v

    # remove duplicates. for pairs not involving the ends of the original string
    # it's just doubled since each letter is the start of one pair and end of another pair
    # for the first and last pair of the string one letter is not duplicated so handle the
    # math slightly differently
    for k,v in dist.items():
        if k not in orig_ends:
            dist[k] = dist[k]/2
        else:
            dist[k] = (dist[k]+1)/2
    #print(f"{graph}")
    #print(f"{dist}")
    values = dist.values()
    print(f"{max(values) - min(values)}")
