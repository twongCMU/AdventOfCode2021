#!/usr/bin/python3

import math
data = []
with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(int(v))


count = 0
for i in range(1, len(data)-2):
    a = data[i-1] + data[i] + data[i+1]
    b = data[i] + data[i+1] + data[i+2]

    if b > a:
        count+=1
print(f"{count}")
