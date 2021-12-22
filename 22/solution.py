#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import itertools
# defaultdict(str)
# defaultdict(int)
# indent shift = ctrl+c >
#guessed 392, 381
data = []


with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)


# 101 since it's -50 to 50 so that's 50+50+1 for the zero
graph = np.zeros((101,101,101), bool)


for row in data:
    (state, rest) = row.split()
    assert state == "on" or state == "off"

    (x, y, z) = rest.split(",")
    print(f"Command {state} {x} {y} {z}")
    x = x[2:]
    x = x.split("..")
    for i in range(2):
        x[i] = int(x[i])
        if x[i] < -50:
            x[i] = -50
        elif x[i] > 50:
            x[i] = 50

    y = y[2:]
    y = y.split("..")
    for i in range(2):
        y[i] = int(y[i])
        if y[i] < -50:
            y[i] = -50
        elif y[i] > 50:
            y[i] = 50

    z = z[2:]
    z = z.split("..")
    for i in range(2):
        z[i] = int(z[i])
        if z[i] < -50:
            z[i] = -50
        elif z[i] > 50:
            z[i] = 50

    count = 0

    if x[0] == x[1] or y[0] == y[1] or z[0] == z[1]:
        continue
    
    for i in range(x[0], x[1]+1):
        for j in range(y[0], y[1]+1):
            for k in range(z[0], z[1]+1):
                if state == "on":
                    graph[i][j][k] = True
                    count+=1
                else:
                    count+=1
                    graph[i][j][k] = False

    print(f"Toggled {count}")
count = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if graph[i][j][k]:
                count+=1
print(f"{count}")
    
        

    
