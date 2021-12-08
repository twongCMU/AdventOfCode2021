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

count = 0
for d in data:
    (_, back) = d.split(" | ")
    letters = back.split(" ")

    for l in letters:
        if len(l) == 2 or len(l) == 3 or len(l) == 4 or len(l) == 7:
            count+=1




print(f"{count}")
