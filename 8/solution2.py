#!/usr/bin/python3

import math
import numpy as np
import re
import itertools
from copy import deepcopy
data = []
with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

count = 0
values = {}
values[5] = []

valid = {}
valid[0] = ["a","b","c","e","f","g"]
valid[1] = ["c","f"]
valid[2] = ["a","c","d","e","g"]
valid[3] = ["a","c","d","f","g"]
valid[4] = ["b","c","d","f"]
valid[5] = ["a","b","d","f","g"]
valid[6] = ["a","b","d","e","f","g"]
valid[7] = ["a","c","f"]
valid[8] = ["a","b","c","d","e","f","g"]
valid[9] = ["a","b","c","d","f","g"]

list1 = list("abcdefg")
list2 = list("abcdefg")

big_sum = 0
for d in data:
    print(f"Looking at one {big_sum}")
    (front, back) = d.split(" | ")
    letters = front.split(" ")
    valid_test = []
    for l in letters:
        valid_test.append(sorted(list(l)))
    
    # generate a random mapping of numbers to letters
    for perm in itertools.permutations(list1):
        mapping = {}
        for i in range(7):
            mapping[list2[i]] = perm[i]

        valid_test_temp = deepcopy(valid_test)

        # apply the mapping to the input strings
        for i in range(10):
            for j in range(len(valid_test_temp[i])):
                valid_test_temp[i][j] = mapping[valid_test_temp[i][j]]

        #print(f"New mapping is {valid_test_temp}")

        # compare the mapped input to the actual 7 segment layout and look for a match
        found_all = True
        for i in range(10):
            match = False
            valid_test_temp[i].sort()
            for j in range(10):
                #print(f"Comparing {valid[j]} to {valid_test_temp[i]}")
                if valid[j] == valid_test_temp[i]:
                    match = True
                    break

            if match is False:
                found_all = False
                break
            
        if found_all is True:
            #print(f"Found a match {mapping}")
            # apply mapping to output values to get segmented display
            output = back.split(" ")
            res = ""
            for o in output:
                #print(f"Output {sorted(list(o))}")
                new_output = []
                for a in list(o):
                    new_output.append(mapping[a])
                new_output.sort()
                for i in range(10):
                    if valid[i] == new_output:
                        #print(f"{new_output} = {i}")
                        res += f"{str(i)}"
                        break

            #print(f"Final {res}")
            big_sum += int(res)


print(f"Done! {big_sum}")

