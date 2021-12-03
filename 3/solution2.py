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

def split_data(d, index, mode):
    print(f"Split: {len(d)} {index} {mode}")
    res0 = []
    res1 = []

    for one_d in d:
        if one_d[index] == "0":
            res0.append(one_d)
        else:
            res1.append(one_d)

    if mode == "greater":
        if len(res0) > len(res1):
            return res0
        # also return 1 on a tie
        return res1
    else:
        # also return 0 on a tie
        if len(res0) <= len(res1):
            return res0
        return res1

for m in ["greater", "less"]:
    current_data = data.copy()
    index = 0
    while len(current_data) > 1:
        current_data = split_data(current_data, index, m)
        print(f"Got back {len(current_data)}")
        index += 1

    print(f"{m}: {int(current_data[0], 2)}")
    


