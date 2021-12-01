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

last = None
count = 0
for d in data:
    if last is None:
        last = d
        continue
    if last is not None and d > last:
        count += 1
        last = d
    else:
        last = d
print(f"{count}")
