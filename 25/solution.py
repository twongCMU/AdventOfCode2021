#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import itertools
# defaultdict(str)
# defaultdict(int)
# indent shift = ctrl+c >

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

graph = np.zeros((len(data), len(data[0])), str)
for i in range(len(data)):
    for j in range(len(data[0])):
        graph[i][j] = "."
            
for i, row in enumerate(data):
    for j, c in enumerate(row):
        graph[i][j] = c

def print_g(graph):
    for i in range(len(data)):
        print("")
        for j in range(len(data[0])):
            print(f"{graph[i][j]}", end='')
print_g(graph)
print("----")
def one_step(graph, which):
    new_graph = np.zeros((len(data), len(data[0])), str)
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_graph[i][j] = "."
    moves = 0

    if which == ">":
        for i in range(len(data)):
            for j in range(len(data[0])):
                if graph[i][j] == ".":
                    continue

                if graph[i][j] == "v":
                    new_graph[i][j] = "v"
                    continue
                    
                next_j = j+1
                if next_j == len(data[0]):
                    next_j=0

                can_move = True
                if graph[i][next_j] != ".":
                    can_move = False

                if can_move:
                    moves += 1
                    #print(f"Moving {i}{j} to {next_j}")
                    new_graph[i][next_j] =  graph[i][j]
                else:
                    new_graph[i][j] =  graph[i][j]
        return(moves, new_graph)



    for i in range(len(data)):
        for j in range(len(data[0])):
            if graph[i][j] == ".":
                continue

            if graph[i][j] == ">":
                new_graph[i][j] = ">"
                continue
                    
            next_i = i+1
            if next_i == len(data):
                next_i=0

            can_move = True
            if graph[next_i][j] != ".":
                can_move = False

            if can_move:
                moves += 1
                new_graph[next_i][j] =  graph[i][j]
            else:
                new_graph[i][j] =  graph[i][j]

    return (moves, new_graph)

moves =1
step = 0
while moves > 0:
    (moves1, new_graph) = one_step(graph, ">")
    graph = new_graph
    moves = moves1
    #print_g(graph)
    #print(f"{moves}")
    (moves2, new_graph) = one_step(graph, "v")
    graph = new_graph
    moves += moves2
    
    step += 1
    #print_g(graph)
    print(f"{step} {moves}")

print(f"done {step}")
    
