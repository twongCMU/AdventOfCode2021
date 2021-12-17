#!/usr/bin/python3

import math
import numpy as np
import re

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)



#target area: x=156..202, y=-110..-69
def simulate(x, y, x_v, y_v):
    x_v_init = x_v
    while 1:
        if 156<=x<=202 and -110 <= y <= -69:
        #if 20<=x<=30 and -10 <= y <= -5:
            # hit
            return 0

        if x > 202:
            # failed
            return 1

        if y < -110:
            # failed
            return 2
        
        x += x_v
        y += y_v

        x_v -= 1
        if x_v < 0:
            x_v = 0
        y_v -= 1


distinct = set()

for i in range(205):#angle
    for j in range(1000):#velocity
        print(f"Angle {i} vel {j} highest so far {len(distinct)}")
        ret = simulate(0,0,i,j)
        if ret == 0:
            distinct.add((i,j))

        ret = simulate(0,0,i,-1*j)
        if ret == 0:
            distinct.add((i,-1*j))

print(f"high is {len(distinct)}")
            
