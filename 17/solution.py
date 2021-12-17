#!/usr/bin/python3

import math
import numpy as np
import re

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)



#target area: x=156..202, y=-110..-69
def simulate(x, y, x_v, y_v):

    highest_y = 0
    while 1:
        if y > highest_y:
            highest_y = y
        if 156<=x<=202 and -110 <= y <= -69:
        #if 20<=x<=30 and -10 <= y <= -5:
            # hit
            return (0, highest_y)

        if x > 202:
            # failed
            return (1, highest_y)

        if y < -110:
            # failed
            return (2, highest_y)
        
        x += x_v
        y += y_v
    
        x_v -= 1
        if x_v < 0:
            x_v = 0
        y_v -= 1


highest_est_y = 0
for i in range(90, 1, -1):#angle
    for j in range(10000):#velocity
        print(f"Angle {i} vel {j} highest so far {highest_est_y}")
        (ret, h_y) = simulate(0,0,i,j)
        if ret == 0:
            if h_y > highest_est_y:
                highest_est_y = h_y
            continue
print(f"high is {highest_est_y}")
            
