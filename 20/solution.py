#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import itertools
# defaultdict(str)
# defaultdict(int)
import sys
np.set_printoptions(threshold=sys.maxsize)
data = []


with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

enhance = data[0]

graph = np.zeros((300,300), bool)
x_start=100
y_start=100

for i, row in enumerate(data[1:]):
    for j, c in enumerate(row):
        graph[y_start+i][x_start+j] = True
        if c == ".":
            graph[y_start+i][x_start+j] = False

def print_graph(graph):
    for i in range(300):
        for j in range(300):
            if graph[i][j]:
                print("#", end='')
            else:
                print(".", end='')
        print("")
        
for loop in range(50):
    #print_graph(graph)
    new_graph = np.zeros((300,300), bool)

    # set the border rows and columns manually since we can't check a 3x3 off the
    # edge of our datastruture even if it is supposedly infinite
    new_val = False
    if not graph[0][0] and enhance[0] == ".":
        print(f"{loop} {graph[0][0]} setting false")
        new_val = False
    if not graph[0][0] and enhance[0] == "#":
        print(f"{loop} {graph[0][0]} setting true")
        new_val = True
    if graph[0][0] and enhance[511] == ".":
        print(f"{loop} {graph[0][0]} setting false")
        new_val = False
    if graph[0][0] and enhance[511] == "#":
        print(f"{loop} {graph[0][0]} setting true")
        new_val = True
    for i in range(300):
        new_graph[i][0] = new_val
        new_graph[i][300-1] = new_val
        new_graph[0][i] = new_val
        new_graph[300-1][i] = new_val

    # check each 3x3 sub grid and put the result in new_graph
    for i in range(1,300-1):
        for j in range(1,300-1):
            bin_s = ""
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    #print(f"{i} {a} {j} {b} {i+a} {j+b} {graph[i+a][j+b]}")
                    if graph[i+a][j+b]:
                        bin_s += "1"
                    else:
                        bin_s += "0"
            e = enhance[int(bin_s, 2)]
            #print(f"at loop{loop} {i},{j} got {e} for {bin_s}")
            if e == ".":
                new_graph[i][j] = False
            else:
                new_graph[i][j] = True
    # swap graphs
    graph = new_graph


count = 0
for i in range(300):
    for j in range(300):
        if graph[i][j]:
            count+= 1
print(f"count {count}")

    
