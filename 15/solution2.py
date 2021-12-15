#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import sys
np.set_printoptions(threshold=sys.maxsize)
import datetime
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

graph = np.zeros((height*5, width*5), np.uint32)

memoize = np.zeros((height*5, width*5), np.uint32)
for i_tile in range(5):
    for j_tile in range(5):
        for i in range(width):
            for j in range(height):
                real_i = (i_tile*width)+i
                real_j = (j_tile*width)+j
                real_value = int(data[j][i]) + i_tile + j_tile
                while real_value > 9:
                    real_value -= 9
                
                graph[real_j][real_i] = real_value
                memoize[real_j][real_i] = -1

width *=5
height *=5
paths = []
paths.append(((0,0), 0))

while len(paths):
    #print(f"Paths is {paths}")
    (last, risk) = paths.pop(0)
    #print(f"at {route[-1]} with risk {risk}")
    (x,y) = last

    # The memoization info might have been updated since we entered the queue
    # so check if this entry's risk is still worth pursuing
    if risk > memoize[y][x]:
        continue

    # try going left
    if x > 0:
        new_risk = risk + graph[y][x-1]
        if new_risk < memoize[y][x-1]:
            #print(f"new risk left {new_risk}")
            memoize[y][x-1] = new_risk
            paths.append(((x-1, y), new_risk))
    # try going right
    if x < width-1:
        new_risk = risk + graph[y][x+1]
        if new_risk < memoize[y][x+1]:
            #print(f"new risk right {new_risk}")
            memoize[y][x+1] = new_risk
            paths.append(((x+1, y), new_risk))
    # try going up
    if y > 0:
        new_risk = risk + graph[y-1][x]
        if new_risk < memoize[y-1][x]:
            #print(f"new risk up {new_risk}")
            memoize[y-1][x] = new_risk
            paths.append(((x, y-1), new_risk))
    # try going down
    if y < height-1:
        new_risk = risk + graph[y+1][x]
        if new_risk < memoize[y+1][x]:
            #print(f"new risk down {new_risk}")
            memoize[y+1][x] = new_risk
            paths.append(((x, y+1), new_risk))


memoize[0][0] = 0
print(f"{memoize}")
print(f"Final: {memoize[-1][-1]}")
