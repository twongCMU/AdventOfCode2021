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

def flash(o):
    count = 0 #how many flashes
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if o[i][j] > 9:
                o[i][j] = -9999
                count += 1
                for x in [-1, 0 , 1]:
                    for y in [-1, 0, 1]:
                        if i+x >= 0 and i+x < 10 and j+y >= 0 and j+y < 10:
                            o[i+x][j+y] += 1

    return (o, count)

total_flashes = 0
for i in range(100):
    # incr everything
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            o[i][j]+=1

            
    count = 1
    while count:
        (o, count) = flash(o)
        total_flashes += count
        
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if o[i][j] < 0:
                o[i][j] = 0

print(f"{total_flashes}")
