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

primary_scanner = 0

matches_required = 66
"""
Found 66 between 0 and 1
Found 66 between 1 and 3
Found 66 between 1 and 4
Found 66 between 2 and 4

0 x, y, z
90 x, z, -y
180 x, -y, -z
270 x, -z, y

Found 66 between 0 and 1
candidate scanner 1
(68, -1246, -43) 12
(1, -1, 1) 11

So, scanner 4 is at -20,-1133,1061 (relative to scanner 0).

scanner 0           scanner 4
(459, -707, 401)  (-660, -479, -426)

"""
def rotate_sensor(b):
    (x,y,z) = b

    res = []
    for r in [(x,y,z), (x,z,-1*y), (x,-1*y,-1*z), (x,-1*z,y)]:
        for f in flip_sensor(r):
            res.append(f)
    return res

def flip_sensor(b):
    (x,y,z) = b
    return [(x,y,z),
            (z, y, -1*x),
            (-1*x, y, -1*z),
            (-1*z, y, x),
            (y, -1*x, z),
            (-1*y, x, z)]


with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

scanner_distances = {}
scanner_points = {}
max_s_id = 0
scanner_id = None
scanner_ids = set()
for row in data:
    if "scanner" in row:
        value = row.split()
        scanner_id = int(value[2])
        max_s_id = scanner_id
        scanner_points[scanner_id] = set()
        scanner_ids.add(scanner_id)
    else:
        (x,y,z) = row.split(",")
        #scanners[scanner_id][(int(x),int(y),int(z))] = {}
        scanner_points[scanner_id].add((int(x),int(y),int(z)))

scanner_locations = [(0,0,0)]
# don't want to check scanner 0 against itself
scanner_ids.remove(primary_scanner)
more_than_one = 0
while len(scanner_ids):
    # compute the distances between each pair of beacons that a given sensor can see if we haven't done so already
    # after the first loop this should only compute for the primary scanner since we've updated its points
    # add primary scanner here manually since it is not in the list of scanner_ids
    for id in list(scanner_ids) + [primary_scanner]:
        if id in scanner_distances:
            continue

        scanner_distances[id] = {}
        for (a,b) in itertools.permutations(scanner_points[id],2):
            distance = math.dist(a,b)
            if distance not in scanner_distances[id]:
                scanner_distances[id][distance] = []
            if a > b and (a,b) not in scanner_distances[id][distance]:
                scanner_distances[id][distance].append((a,b))
            elif b >= a and (b,a) not in scanner_distances[id][distance]:
                scanner_distances[id][distance].append((b,a))
            if len(scanner_distances[id][distance]) > 1:
                more_than_one+=1
            #assert [id][distance]) == 1, f"{id} {distance} {scanner_distances[id][distance]}"
        #print(f"More than one match for distance {distance} {more_than_one}")
    candidate_scanner = None
    for s2 in scanner_ids:
        distances = scanner_distances[primary_scanner]

        same_count = 0
        for d in distances:
            if d in scanner_distances[s2]:
                same_count += 1

        if same_count >= matches_required:
            print(f"Found {same_count} common distances between {primary_scanner} and {s2}")
            assert same_count >= 66
            candidate_scanner = s2
            break

    #candidate_scanner = 4
    # could use itertools.permutations for this but I think better if I can see this table when I'm coding
    translate = [(1,1,1),
                 (-1,1,1),
                 (1,-1,1),
                 (1,1,-1),
                 (-1,-1,1),
                 (1,-1,-1),
                 (-1,1,-1),
                 (-1,-1,-1)]

    print(f"candidate scanner {candidate_scanner} {len(scanner_ids)} remain")
    global_equiv = {}

    equiv = defaultdict(int)

    s1_d = scanner_distances[primary_scanner]
    s2_d = scanner_distances[candidate_scanner]

    # if we have points two lines in two coordinate systems with the same distance
    # we can assume that some of those points are equal to each other but we don't
    # know which ones. We'll note all possibilities here then sort it out later
    for d1 in s1_d:
        if d1 in s2_d:
            for (s1_c1, s1_c2) in scanner_distances[primary_scanner][d1]:
                for (s2_c1, s2_c2) in scanner_distances[candidate_scanner][d1]:

                    equiv[(s1_c1, s2_c1)] += 1
                    equiv[(s1_c2, s2_c1)] += 1
                    equiv[(s1_c1, s2_c2)] += 1
                    equiv[(s1_c2, s2_c2)] += 1

    # the equivalent points are the ones that appeared the most often in our accounting
    print(f"Overlapping between {primary_scanner}  {candidate_scanner}")
    for e, v in equiv.items():
        #assert v == 1 or v == 11
        #print(f"{v}")
        if v >= 11:
            (s1_temp, s2_temp) = e
            global_equiv[s1_temp] = s2_temp
            #print(f"{s1_temp}  {s2_temp}")
    #print(f"global equiv has {len(global_equiv)}")
    # now that we know the equivalent points between two sensors we can start guessing
    # how to map between them. Add all combinations of +/- offsets then we'll see which
    # one shows up the most often
    p = defaultdict(int)
    which_translate = defaultdict(int)
    for (a,b) in global_equiv.items():
        (ax,ay,az) = a
        b_list = rotate_sensor(b)
        for t in translate:
            (dx, dy, dz) = t
            for rot_i, (bx, by, bz) in enumerate(b_list):
                p[(ax+(dx*bx), ay+(dy*by), az+(dz*bz), rot_i)] += 1

                # See which +/- of the various axes produced a common origin
                # only one t should have anything but we track multiples for debugging
                if p[(ax+(dx*bx), ay+(dy*by), az+(dz*bz), rot_i)] > 1:
                    which_translate[(t, rot_i)]+=1

    #print(f"{p.keys()}")
    # candidate scanner's position in primary scanner's coordinate system
    s1_origin = None
    best_translate = None

    #sorting this keeps us out of sync with which_translate
    max_v = 0
    for i, v in p.items():
        if v > max_v:
            max_v = v
            
    for i, v in p.items():
        if v == max_v:
            #print(f"best origin {i} {v}")
            s1_origin = i
            if i[3] == 0:
                break
            
    for i, v in which_translate.items():
        if v == max_v-1:
            #print(f"best translate {i} {v}")
            best_translate = i
            if i[1] == 0:
                break

    # how to get from the new origin location in old origin coords to the points
    # so we can translate the rest of the new origin's points to old origin coords
    (s1o_x, s1o_y, s1o_z, _) = s1_origin
    ((d_x, d_y, d_z), rot) = best_translate

    # best_translate is how to get from the point to the origin. Flip it to get from origin to point
    d_x *= -1
    d_y *= -1
    d_z *= -1

    # safety check. Make sure we can get from the candidate origin in origin 0's coords to the points in common
    for k,v in global_equiv.items():
        (s1_x, s1_y, s1_z) = k # point in origin 0 space
        #(s2_x, s2_y, s2_z) = v # point in origin 1 space
        (s2_x, s2_y, s2_z) = rotate_sensor(v)[rot]
        # s1_origin in origin 0 space +  point in origin 1 space*best_translate = point in origin 0 space
        #print(f"{s1o_x}+({s2_x}*{d_x}) {s1o_x+(s2_x*d_x)} == {s1_x}")
        #print(f"{s1o_y}+({s2_y}*{d_y}) {s1o_y+(s2_y*d_y)} == {s1_y}")
        #print(f"{s1o_z}+({s2_z}*{d_z}) {s1o_z+(s2_z*d_z)} == {s1_z}")

        assert s1o_x+(s2_x*d_x) == s1_x
        assert s1o_y+(s2_y*d_y) == s1_y
        assert s1o_z+(s2_z*d_z) == s1_z

    scanner_locations.append((s1o_x, s1o_y, s1o_z))
    # now add points in origin 1's knowledge into origin 0's coordinate system
    #print(f"List of new points")
    for p in scanner_points[s2]:
        #(px, py, pz) = p
        (px, py, pz) = rotate_sensor(p)[rot]

        nx = s1o_x+(px*d_x)
        ny = s1o_y+(py*d_y)
        nz = s1o_z+(pz*d_z)


        if ((nx,ny,nz) not in scanner_points[primary_scanner]):
            #print(f"Added {nx},{ny},{nz}")
            scanner_points[primary_scanner].add((nx,ny,nz))

    print(f"Part 1: Number of points after merging is {len(scanner_points[0])}")
    #print(f"points after merging is {sorted(scanner_points[0])}")
    # update accounting
    del scanner_distances[primary_scanner] # we added more points to scanner 0 so signal that we'll have to do updates
    del scanner_distances[s2] # we folded this into scanner 0
    scanner_ids.remove(s2)



manhattan = []
for (s1, s2) in itertools.permutations(scanner_locations,2):
    (s1x, s1y, s1z) = s1
    (s2x, s2y, s2z) = s2
    manhattan.append(abs(s1x-s2x)+abs(s1y-s2y)+abs(s1z-s2z))
print(f"Part 2: {max(manhattan)}")
