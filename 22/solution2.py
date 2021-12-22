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
from multiprocessing import Pool

with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

#data = ["on x=1..10,y=1..10,z=1..10"]
        #"on x=11..20,y=11..20,z=11..20"]
# 101 since it's -50 to 50 so that's 50+50+1 for the zero

on_ranges = []
count = 0

x_points = set()
y_points = set()
z_points = set()
boxes = []

# Make a full list of each x,y,z coord that is involved in the bounds of the input cube
# then we also include a 1 point border around that cube so that we can handle overlap
# That is, if I have a cube that ends at X=10 and another that starts at X=10, we have
# a duplicate. So we insert a point at X=9 so that the first cube now ends at 9 
for layer, row in enumerate(data):
    print(f"processing row {layer}")
    (state, rest) = row.split()
    assert state == "on" or state == "off"

    (x, y, z) = rest.split(",")
    #print(f"Command {state} {x} {y} {z}")
    x = x[2:]
    x = x.split("..")
    for i in range(2):
        x_points.add(int(x[i]))
    x_points.add(int(x[1])+1)
    x_points.add(int(x[0])-1)

    y = y[2:]
    y = y.split("..")
    for i in range(2):
        y_points.add(int(y[i]))
    y_points.add(int(y[1])+1)
    y_points.add(int(y[0])-1)
        
    z = z[2:]
    z = z.split("..")
    for i in range(2):
        z_points.add(int(z[i]))
    z_points.add(int(z[1])+1)
    z_points.add(int(z[0])-1)

  
    boxes.append((state, int(x[0]), int(x[1]), int(y[0]), int(y[1]), int(z[0]), int(z[1])))

x_keys = sorted(list(x_points))
y_keys = sorted(list(y_points))
z_keys = sorted(list(z_points))

print(f"Collected list of points x {len(x_keys)} y {len(y_keys)} z {len(z_keys)}")
#print(f"{x_keys}")
#print(f"{y_keys}")
#print(f"{z_keys}")
x_keys_lookup = {}
y_keys_lookup = {}
z_keys_lookup = {}

for i, v in enumerate(x_keys):
    x_keys_lookup[v] = i
for i, v in enumerate(y_keys):
    y_keys_lookup[v] = i
for i, v in enumerate(z_keys):
    z_keys_lookup[v] = i

volumes = {}
# We have chopped up the space into smaller boxes represented by the borders of all of the inputs
# now, we can fill out a matrix where each index into the matrix represents one of the border points
graph = np.zeros((len(x_keys), len(y_keys), len(z_keys)), bool)
for box_id, b in enumerate(boxes):
    (state, x0, x1, y0, y1, z0, z1) = b
    x0 = x_keys_lookup[x0]
    x1 = x_keys_lookup[x1]
    y0 = y_keys_lookup[y0]
    y1 = y_keys_lookup[y1]
    z0 = z_keys_lookup[z0]
    z1 = z_keys_lookup[z1]
    print(f"Marking box {box_id}/{len(boxes)} This one has {abs(x0-x1)*abs(y0-y1)*abs(z0-z1)}")

    for i in range(min(x0,x1), max(x0,x1)+1):
        for j in range(min(y0,y1), max(y0,y1)+1):
            for k in range(min(z0,z1), max(z0,z1)+1):
                if state == "on":
                    graph[i][j][k] = True
                else:
                    graph[i][j][k] = False
        
print(f"Done marking boxes")

# Now compute the volumes of each "on" box
count = 0
for i in range(len(x_keys)-1):
    print(f"Counting volumes {i}/{len(x_keys)} This one has {len(y_keys)*len(z_keys)} updates")
    x_start = x_keys[i]
    x_end   = x_keys[i+1]
    for j in range(len(y_keys)-1):
        y_start = y_keys[j]
        y_end   = y_keys[j+1]
        for k in range(len(z_keys)-1):
            z_start = z_keys[k]
            z_end   = z_keys[k+1]

            if graph[i][j][k]:
                volume= (abs(x_end - x_start)) * (abs(y_end - y_start)) * (abs(z_end - z_start))
                #print(f"Adding {volume} for {x_start},{x_end}/{y_start},{y_end}/{z_start},{z_end}")
                count +=  volume



print(f"count is {count}")
"""

for i in range(x_keys):
    for j in range(y_keys):
        for k in range(z_keys):
"""
print(  " goal is 2758514936282235")
