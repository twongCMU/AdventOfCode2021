#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import itertools
# defaultdict(str)
# defaultdict(int)
# indent shift = ctrl+c >

data = []



start = [3,7]
#start = [4,8]
score = [0,0]
offset = 0

done = -1
rolls = 0
def get_next(offset):
    ret = offset+1
    if ret > 100:
        ret = 1

    return ret

while done == -1:
    for p in range(2):
        #get = int(((offset*(offset+1))/2)) - int((((offset-3)*((offset-2)))/2))
        get = 0
        for i in range(3):
            offset = get_next(offset)
            get += offset
        
        rolls += 3
        start[p] = (start[p]+ get) % 10
        if start[p] == 0:
            start[p] = 10

        score[p]+=start[p]
        if score[p] >= 1000:
            done = p
            break
        print(f"Player {p} score {score[p]} offset {offset} sum was {get} pos {start[p]}")


        
winner = 0
if done== 0:
    winner = 1
print(f"{score[winner]} * {rolls}")
print(f"{score[winner] * rolls}")
    


    
