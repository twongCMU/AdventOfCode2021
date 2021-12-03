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

count1 = [0]*len(data[0])
count0 = [0]*len(data[0])
for v in data:
    for i, d in enumerate(v):
        if d == "1":
            count1[i]+=1
        else:
            count0[i]+=1

res = ""
res2 = ""
for i in range(len(count0)):
    if count0[i] > count1[i]:
        res += "0"
        res2 += "1"
    else:
        res += "1"
        res2 += "0"
print(f"{int(res,2)}")
print(f"{int(res2,2)}")
print(f"{int(res,2)*int(res2,2)}")
