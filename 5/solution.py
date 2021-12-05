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


points = {}
#hacky initialization
for i in range(1000000):
    points[i] = {}
for v in data:
    (start, end) = v.split(" -> ")
    (s1, s2) = start.split(",")
    (e1, e2) = end.split(",")
    s1 = int(s1)
    s2 = int(s2)
    e1 = int(e1)
    e2 = int(e2)

    # it is not efficient to handle the x change and y change separately but
    # I couldn't think of how to do it compactly with time pressure
    if s1 == e1:
        # swap the values so they're increasing. Should have just decided if
        # range's step was 1 or -1
        if e2 < s2:
            temp = e2
            e2 = s2
            s2 = temp
        print(f"looking at {v}: {s1} {s2}:{e1} {e2}")
        for i in range(s2, e2+1):
            if i not in points[s1]:
                points[s1][i] = 0

            points[s1][i] += 1
    elif s2 == e2:
        if e1 < s1:
            temp = e1
            e1 = s1
            s1 = temp
        print(f"looking at {v}: {s1} {s2}:{e1} {e2}")
        for i in range(s1, e1+1):
            if s2 not in points[i]:
                points[i][s2] = 0
            points[i][s2] += 1

# misread the problem so I computed some extra stuff
maxv = 0
maxi = 0
maxj = 0
overlap_count = 0
for i in points.keys():
    for j in points[i]:
        if points[i][j] > 1:
            overlap_count +=1
        if points[i][j] > maxv:
            maxv = points[i][j]
            maxi = i
            maxj = j
            
print(f"Res {maxv} {maxi} {maxj} {overlap_count}")
