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

def get_basin_size(data, points, height, width, count, seen_points):
    (i, j) = points.pop(0)

    seen_points.append((i,j))
    if i > 0 and data[i-1][j] != 9:
        if (i-1, j) not in seen_points and (i-1, j) not in points:
            points.append((i-1, j))
            count+=1
        
    if j > 0 and data[i][j-1] != 9:
        if (i, j-1) not in seen_points and (i, j-1) not in points:
            points.append((i, j-1))
            count+=1
        
    if i < (width-1) and data[i+1][j] != 9:
        if (i+1, j) not in seen_points and (i+1, j) not in points:
            points.append((i+1, j))
            count+=1
        
    if j < (height-1) and data[i][j+1] != 9:
        if (i, j+1) not in seen_points and (i, j+1) not in points:
            points.append((i, j+1))
            count+=1

    return (points, count, seen_points)

# compute the low points
basins = []
low_points = []
for i in range(width):
    for j in range(height):
        if check_neighbors(data_grid, i, j, height, width):
            low_points.append((i,j))


# walk around looking for the basin size iteratively by putting new points into a queue
for (i,j) in low_points:
    print(f"basin {i},{j}")
    points = [(i,j)]
    basin_size = 1
    seen_points = []
    while len(points):
        (points, basin_size, seen_points) = get_basin_size(data_grid, points, height, width, basin_size, seen_points)
        print(f"{points}")
                
    print(f"Basin size {basin_size}")
    basins.append(basin_size)

basins.sort()
print(f"{basins}")
print(f"{basins[-1]*basins[-2]*basins[-3]}")
