#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import itertools
# defaultdict(str)
# defaultdict(int)
# indent shift = ctrl+c >

dice=[1,2,3]



#start = [3,7]
#start = [4,8]
score = [0,0]
offset = 0


rolls = 0



wins = {0:defaultdict(int),
        1:defaultdict(int)}


paths = defaultdict(int)
# depth, start0, start1, score0, score1, next_player. Value is number of times this combination was seen
paths[(0, 3, 7, 0 ,0, 0)] = 1 # input
#paths[(0, 4, 8, 0 ,0, 0)] = 1 # example

# a copy of the keys in paths but we'll keep this list so we can pick a fresh one each round
# I think this is not an ideal way to do it especially due to the O(n) lookup later on
# but the keys in paths don't change so it's hard to work on a fresh key each time
next_list = [list(paths.keys())[0]]

loop_count= 0
while len(next_list):
    # collect the data for this situation
    first_key = next_list.pop(0)
    (d, start0, start1, score0, score1, next_player) = first_key
    first_value = paths[first_key]

    # until we decide what to do, set this to zero instances seen of this context
    paths[first_key] = 0

    if loop_count % 10000 == 0:
        print(f"{loop_count}/{len(paths.keys())} winners {wins} {first_key} {first_value}")


    # iterate over each possible sequence of 3 dice rolls
    for rolls in itertools.product([1,2,3], repeat=3):
        start = [start0, start1]
        score = [score0, score1]

        # apply the rolls and scores
        roll_sum = sum(rolls)
        start[next_player] = (start[next_player]+ roll_sum) % 10
        if start[next_player] == 0:
            start[next_player] = 10
                
        score[next_player]+=start[next_player]

        # if we're done, track the winner
        if score[next_player] >= 21:
            #print(f"winner at depth {d+3} roll {rolls} score {score[next_player]} position {start[next_player]} player {next_player}")
            # add winner
            cur_depth = d+3
            wins[next_player][cur_depth] += first_value
            continue
        # if we're not done, add the new context to the trackint
        else:
            temp_player = 0
            if next_player == 0:
                temp_player = 1
            #print(f"{d+3} {start} {score} {temp_player} {rolls}")
            next_key = (d+3, start[0], start[1], score[0], score[1], temp_player)
            paths[next_key] += first_value

            # I think this O(n) lookup costs the most CPU time but it still runs in
            # 48 seconds on my machine so I'm too lazy to fix
            if next_key not in next_list:
                next_list.append(next_key)
    loop_count +=1

print(f"loop count {loop_count}")
print(f"{wins}")

for i in [0,1]:
    count = 0
    for k,v in wins[i].items():
        count += v
    print(f"{count}")

        
