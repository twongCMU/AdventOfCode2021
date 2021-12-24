#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import itertools
# defaultdict(str)
# defaultdict(int)
# indent shift = ctrl+c >

import sys
np.set_printoptions(threshold=sys.maxsize)
data = []

#####################
#####################
## NOTE: the real solution came from solver.py. This solution.py ended up being useless
#####################
#####################

with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)


import alu

#test = alu.ALU()
#test_arg
#for i in range(990429746, 990429748):
#for i in range(100):
#i = 99999999999999-3560620058
#i=99999999999999
start="8765432198765"
     #i=99999999999999
start = "99999999999999"
start = "00000000000000"
ret = 0
"""
for digit in range(14):
    print(f"start is now {start} on digit {digit}")
    lowest_score = 999999999999
    lowest_index = None
    for i in range(1,10):
        f = alu.ALU()
        inputs = list(str(start))

        a = list(inputs)
        a[digit]= f"{i}"
        inputs = a
        #print(f"Using {inputs}")
        for j in range(len(inputs)):
            inputs[j] = int(inputs[j])
        
        ret = f.run(data, inputs)
        if ret == 0:
            print(f"Good: {inputs}")
            break
        else:
            print(f"Bad: {inputs} {ret}")
            
            if ret < lowest_score:
                lowest_score = ret
                lowest_index = i

    print(f"Picked {lowest_index} for digit {digit}")
    a = list(start)
    a[digit]=f"{lowest_index}"
    start = ''.join(a)

print(f"start is now {start}")
inputs = list(str(start))
for j in range(len(inputs)):
    inputs[j] = int(inputs[j])
        
ret = f.run(data, inputs)
if ret == 0:
    print(f"Good: {inputs}")
else:
    print(f"Bad: {inputs} {ret}")

print(f"{bin(round(ret))}")
# guessed 11111711191311
"""
"""
start = 11111111111111

count = 0

while True:
    inputs = list(str(start))
    
    for j in range(len(inputs)):
        inputs[j] = int(inputs[j])

    f = alu.ALU()
    ret = f.run(data, inputs)
    if ret == 0:
        print(f"Good: {inputs}")
        break
    else:
        print(f"Bad: {inputs} {ret}")
        start+=1

    if "0" in f"{start}":
        start+=1
    
"""
"""
#start = 11111111111111
start = 99999999999999
for i in range(1,10):
    f = alu.ALU()
    inputs = list(str(start))

    a = list(inputs)
    a[0]= f"{i}"
    inputs = a
    #print(f"Using {inputs}")
    for j in range(len(inputs)):
        inputs[j] = int(inputs[j])
        
    ret = f.run(data, inputs)
    if ret == 0:
        print(f"Good: {inputs}")
        break
    else:
        print(f"Bad: {inputs} {ret}")

"""
start = 99999119191111
#       +++++--+-+----
start = 99999799999999

f = alu.ALU()
inputs = list(str(start))

a = list(inputs)
inputs = a
for j in range(len(inputs)):
    inputs[j] = int(inputs[j])
        
ret = f.run(data, inputs)
if ret == 0:
    print(f"Good: {inputs}")
else:
    print(f"Bad: {inputs} {ret}")

# input #6 divides z by 26 so to get 0 we need to be underthat amount
# digit 1: z=w+2
# digit 2: z=z*26 + (4+w)
# digit 3: z=z*26+(w+8)
# digit 4: z=z*26+(w+7)
# digit 5: z=z*26+(w+12)
# digit 6: z=z/26, x=z%26 - 14. If x == w, z doesn't change after that
# digit 7: z=z/26, x=z%26 - 0     if x == w, z doesn't change after that
# digit 8: z=z*26, x=z%26 +(14+w)
# digit 9: z=z/26, x=z%26 -10  if x == w, z doesn't change
# digit 10: z=z*26 +(w+6)
# digit 11: z=z/26, x=z%26-12 if x==w, z doesn't change after that
# digit 12: z=z/26, x=z%26-3 if x==w, z doesn't change
# digit 13: z=z/26, x=z%26-11 if x==w, z doesn't change
# digit 14: z=z/26, x=z%26-2 if x==w, z doesn't change
