#!/usr/bin/python3

import math
data = []
with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

# [forward, depth, aim]
coords = [0,0,0]

for v in data:
    (dir, c) = v.split(" ")
    c = int(c)
    if dir == "forward":
        coords[0] += c
        coords[1] += c*coords[2]
    if dir == "up":
        coords[2] -= c
    if dir == "down":
        coords[2] += c
print(f"Part 2: {coords} {coords[0]*coords[1]}")
