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

#[forward, depth]
coords = [0,0]

for v in data:
    (dir, c) = v.split(" ")
    c = int(c)
    if dir == "forward":
        coords[0] += c
    if dir == "up":
        coords[1] -= c
    if dir == "down":
        coords[1] += c
print(f"Part 1: {coords} {coords[0]*coords[1]}")


