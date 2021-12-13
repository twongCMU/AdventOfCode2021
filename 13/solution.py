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
            print(f"{len(graph.keys())}")

            


    
