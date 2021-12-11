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

o = np.zeros((10,10), np.int32)
for i, row in enumerate(data):
    for j, v in enumerate(row):
        o[i][j] = int(v)

def flash(o, seen):
    count = 0 #how many flashes
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if o[i][j] > 9:
                seen[(i,j)] = 1
                o[i][j] = -9999
                count += 1
                for x in [-1, 0 , 1]:
                    for y in [-1, 0, 1]:
                        if i+x >= 0 and i+x < 10 and j+y >= 0 and j+y < 10:
                            o[i+x][j+y] += 1

    return (o, count, seen)

total_flashes = 0
for p in range(1, 9999999):
    # incr everything
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            o[i][j]+=1

            
    count = 1
    seen = {}
    while count:
        (o, count, seen) = flash(o, seen)
        total_flashes += count

    print(f"round {p} {len(seen.keys())}")
    if len(seen.keys()) == 100:
        print(f"part 2 round {p}")
        break
    
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if o[i][j] < 0:
                o[i][j] = 0

