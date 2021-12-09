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

data_grid = np.zeros((len(data[0]), len(data)), np.uint8)
height = len(data)
width = len(data[0])
print(f"height {height} width {width}")
for j, row in enumerate(data):
    for i, v in enumerate(list(str(row))):
        data_grid[i][j] = v

def check_neighbors(data, i, j, height, width):
    this = data[i][j]

    if i > 0 and data[i-1][j] <= this:
        return False

    if j > 0 and data[i][j-1] <= this:
        return False

    if i < (width-1) and data[i+1][j] <= this:
        return False

    if j < (height-1) and data[i][j+1] <= this:
        return False

    return True

count = 0
score=0
for i in range(width):
    for j in range(height):
        if check_neighbors(data_grid, i, j, height, width):
            count+=1
            score += (1+data_grid[i][j])
print(f"{count} : {score}")
    
    
        
    
