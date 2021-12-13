#!/usr/bin/python3

import math
import numpy as np
import re

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

data = []


with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

graph = {}
max_x = 0
max_y = 0
for row in data:
    # extract the coordinates and build the list of points
    if "," in row:
        (a, b) = row.split(",")
        a = int(a) # x
        b = int(b) # y
        if a > max_x:
            max_x = a
        if b > max_y:
            max_y = b
        graph[(a,b)] = 1

    # fold along the x axis by updating the points
    if "=" in row:
        (direction, value) = row.split("=")
        value = int(value)
        if direction == "x":
            deletes = []
            adds = []
            for (x, y) in graph.keys():
                if x > value:
                    offset = x - value
                    new_x = value - offset
                    adds.append((new_x, y))
                    deletes.append((x,y))
            for d in deletes:
                del graph[d]

            for a in adds:
                graph[a] = 1

            max_x = value-1

        # fold along the y axis by updating the points
        if direction == "y":
            deletes = []
            adds = []
            for (x, y) in graph.keys():
                if y > value:
                    offset = y - value
                    new_y = value - offset
                    adds.append((x, new_y))
                    deletes.append((x,y))
            for d in deletes:
                del graph[d]

            for a in adds:
                graph[a] = 1

            max_y = value-1

# convert the points into a numpy matrix
print(f"{max_x} {max_y} {graph}")
graph_full = np.zeros((max_y+1, max_x+1), np.int)
for (x,y) in graph.keys():
    graph_full[y][x] = 1

# print out
for row in graph_full:
    print("")
    for column in row:
        if column == 0:
            print(".", end='')
        else:
            print("X", end='')

            


    
