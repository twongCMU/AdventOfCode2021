#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import sys
np.set_printoptions(threshold=sys.maxsize)

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


width = len(data[0])
height = len(data)

graph = np.zeros((height, width), np.uint32)

memoize = np.zeros((height, width), np.uint32)
for i in range(width):
    for j in range(height):
        graph[j][i] = data[j][i]
        memoize[j][i] = -1


paths = []
paths.append(([(0,0)], 0))

while len(paths):
    #print(f"Paths is {paths}")
    (route, risk) = paths.pop(0)
    #print(f"at {route[-1]} with risk {risk}")
    (x,y) = route[-1]

    # try going left
    if x > 0:
        new_risk = risk + graph[y][x-1]
        if new_risk < memoize[y][x-1] and (x-1, y) not in route:
            #print(f"new risk left {new_risk}")
            memoize[y][x-1] = new_risk
            new_route = route.copy()
            new_route.append((x-1, y))
            paths.append((new_route, new_risk))
    # try going right
    if x < width-1:
        new_risk = risk + graph[y][x+1]
        if new_risk < memoize[y][x+1] and (x+1, y) not in route:
            #print(f"new risk right {new_risk}")
            memoize[y][x+1] = new_risk
            new_route = route.copy()
            new_route.append((x+1, y))
            paths.append((new_route, new_risk))
    # try going up
    if y > 0:
        new_risk = risk + graph[y-1][x]
        if new_risk < memoize[y-1][x] and (x, y-1) not in route:
            #print(f"new risk up {new_risk}")
            memoize[y-1][x] = new_risk
            new_route = route.copy()
            new_route.append((x, y-1))
            paths.append((new_route, new_risk))
    # try going down
    if y < height-1:
        new_risk = risk + graph[y+1][x]
        if new_risk < memoize[y+1][x] and (x, y+1) not in route:
            #print(f"new risk down {new_risk}")
            memoize[y+1][x] = new_risk
            new_route = route.copy()
            new_route.append((x, y+1))
            paths.append((new_route, new_risk))


memoize[0][0] = 0
print(f"{memoize}")
print(f"Final: {memoize[-1][-1]}")
