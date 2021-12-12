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
for v in data:
    (a, b) = v.split('-')

    if a not in graph:
        graph[a] = []
    graph[a].append(b)

    if b not in graph:
        graph[b] = []
    graph[b].append(a)

paths = [["start"]]

print(f"mapping {graph}")
path_count = 0
while len(paths):
    p = paths.pop(0)

    cur = p[-1]

    for nxt in graph[cur]:
        if nxt.islower() and nxt in p:
            print(f"throwing out {p} {nxt}")
            continue

        if nxt == "end":
            path_count += 1
            print(f"{p} {nxt}")
            continue

        p2 = p.copy()
        p2.append(nxt)
        paths.append(p2)

    print(f"Paths count {len(paths)} complete {path_count}")
print(f"{path_count}")


    
