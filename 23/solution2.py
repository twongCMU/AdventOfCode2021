#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import itertools
# defaultdict(str)
# defaultdict(int)
# indent shift = ctrl+c >


"""
input
...........
##A#D#B#C##
 #B#C#D#A#

"""

"""
example
...........
##B#C#B#D##
 #A#D#C#A#
"""
graph = np.zeros((5, 11), str)
for i in range(11):
    graph[0][i] = "."
    
graph[1][0] = "#"
graph[1][1] = "#"
graph[1][3] = "#"
graph[1][5] = "#"
graph[1][7] = "#"
graph[1][9] = "#"
graph[1][10] = "#"

graph[2][0] = "#"
graph[2][1] = "#"
graph[2][3] = "#"
graph[2][5] = "#"
graph[2][7] = "#"
graph[2][9] = "#"
graph[2][10] = "#"

#input
graph[1][2] = "A"
graph[2][2] = "D"
graph[3][2] = "D"
graph[4][2] = "B"

graph[1][4] = "D"
graph[2][4] = "C"
graph[3][4] = "B"
graph[4][4] = "C"

graph[1][6] = "B"
graph[2][6] = "B"
graph[3][6] = "A"
graph[4][6] = "D"

graph[1][8] = "C"
graph[2][8] = "A"
graph[3][8] = "C"
graph[4][8] = "A"

#example
"""
graph[1][2] = "B"
graph[2][2] = "D"
graph[3][2] = "D"
graph[4][2] = "A"

graph[1][4] = "C"
graph[2][4] = "C"
graph[3][4] = "B"
graph[4][4] = "D"

graph[1][6] = "B"
graph[2][6] = "B"
graph[3][6] = "A"
graph[4][6] = "C"

graph[1][8] = "D"
graph[2][8] = "A"
graph[3][8] = "C"
graph[4][8] = "A"
"""
#custom
"""
graph[0][1] = "C"
graph[0][5] = "B"
graph[0][9] = "A"
graph[0][10] = "D"
graph[1][2] = "."
graph[2][2] = "A"

graph[1][4] = "."
graph[2][4] = "B"

graph[1][6] = "."
graph[2][6] = "C"

graph[1][8] = "."
graph[2][8] = "D"
"""
letter_index = {"A":2,
                "B":4,
                "C":6,
                "D":8}

letter_cost = {"A":1,
               "B":10,
               "C":100,
               "D":1000}

#        graph, score
states = [(graph, 0)]
seen = {}
def is_success(graph):
    good = 0
    if graph[1][2] ==  "A":
        good+=1
    if graph[4][2] == "A":
        good+=1
    if graph[1][4] == "B":
        good+=1
    if graph[4][4] == "B":
        good+=1
    if graph[1][6] == "C":
        good+=1
    if graph[4][6] == "C":
        good+=1
    if graph[1][8] == "D":
        good+=1
    if graph[4][8] == "D":
        good+=1

    #part 2 add-on
    if graph[2][2] ==  "A":
        good+=1
    if graph[3][2] == "A":
        good+=1
    if graph[2][4] == "B":
        good+=1
    if graph[3][4] == "B":
        good+=1
    if graph[2][6] == "C":
        good+=1
    if graph[3][6] == "C":
        good+=1
    if graph[2][8] == "D":
        good+=1
    if graph[3][8] == "D":
        good+=1

    return good

def is_legal_up(graph, start_x, start_y, end_x):
    # end_y is always 0
    letter = graph[start_y][start_x]
    if letter == ".":
        return False
    index = letter_index[letter]

    # if we are already home in row 2 and everything below us is correct don't move
    if start_x == index:
        correct = True
        for i in range(start_y, 5):
            if graph[i][start_x] != letter:
                correct = False
        if correct:
            return False

    # if somebody is above us. Make sure we don't check our own spot
    for i in range(1, start_y):
        if graph[i][start_x] != ".":
            return False

    # if we are moving up and somebody is in the way in the top row
    for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
        if graph[0][i] != ".":
            return False

    return True

def is_legal_down(graph, start_x, end_x, end_y):
    # assume we will only try to move into our own hole so we don't check that case here
    # start_y is always 0 in this case
    #print(f"Trying {start_x} {end_x},{end_y}")
    letter = graph[0][start_x]
    if letter == ".":
        #print("bad start letter")
        return False
    
    # see if top row is clear
    skip_start = 1# move the check start one spot so we don't see ourselves
    skip_end = 0 
    if end_x < start_x:
        skip_start = 0
        skip_end = -1
    for i in range(min(start_x, end_x)+skip_start, max(start_x, end_x) + 1+ skip_end):
        if graph[0][i] != ".":
            #print(f"top row not clear at {i}")
            return False

    # if we move into our column, everything above our spot and our spot must be clear
    for i in range(1, end_y+1):
        if graph[i][end_x] != ".":
            #print("row 2 not proper")
            return False
        
    # if we move into our column, everything below us must be already correct
    for i in range(end_y+1, 5):
        if graph[i][end_x] != letter:
            #print("row 2 not proper")
            return False

    #print("looks good")
    return True

def do_move(graph, start_x, start_y, end_x, end_y):
    new_g = graph.copy()

    new_g[end_y][end_x] = new_g[start_y][start_x]
    new_g[start_y][start_x] = "."

    distance = 0
    distance += abs(start_y-end_y)
    distance += abs(start_x-end_x)

    cost = letter_cost[new_g[end_y][end_x]] * distance
    #print(f"move cost {cost}")
    return (new_g, cost)

lowest_score = 99999999
iteration = 0
while len(states):
    #for (s,sc) in states:
    #    print(f"{s}")

    # after talking with friends I realize I should sort this by energy (the value of the dict)
    # so that we process the better board states first then as we get to higher energy states
    # there's a higher chance that we can prune it
    (cur_graph, cur_score) = states.pop(0)

    check =(cur_graph[0][0],
            cur_graph[0][1],
            cur_graph[0][2],
            cur_graph[0][3],
            cur_graph[0][4],
            cur_graph[0][5],
            cur_graph[0][6],
            cur_graph[0][7],
            cur_graph[0][8],
            cur_graph[0][9],
            cur_graph[0][10],
            cur_graph[1][2],
            cur_graph[1][4],
            cur_graph[1][6],
            cur_graph[1][8],
            cur_graph[2][2],
            cur_graph[2][4],
            cur_graph[2][6],
            cur_graph[2][8],
            cur_graph[2][2],
            cur_graph[2][4],
            cur_graph[2][6],
            cur_graph[2][8],
            cur_graph[2][2],
            cur_graph[2][4],
            cur_graph[2][6],
            cur_graph[2][8])
             
    if check in seen and cur_score >= seen[check]:
        continue
    seen[check] = cur_score
    
    success_count = is_success(cur_graph)
    print(f"num: {len(states)} this_score:{cur_score} low score: {lowest_score} success: {success_count} iter {iteration}")
    #print(f"{cur_graph}")
    # move from top row down
    for i in range(11):
        letter = cur_graph[0][i]

        if letter == ".":
            continue
        
        if is_legal_down(cur_graph, i, letter_index[letter], 1):
            (new_graph, new_score) = do_move(cur_graph, i, 0, letter_index[letter], 1)
            if is_success(new_graph) == 16:
                #print(f"success {new_graph}")
                if new_score+cur_score<lowest_score:
                    lowest_score = new_score + cur_score
            else:
                #print("appending")
                states.append((new_graph, new_score+cur_score))

        for depth in [2,3,4]:
            if is_legal_down(cur_graph, i, letter_index[letter], depth):
                (new_graph, new_score) = do_move(cur_graph, i, 0, letter_index[letter], depth)
                #print("appending")
                states.append((new_graph, new_score+cur_score))

    # move from hole up to top row
    for i in [2,4,6,8]: # starting x coord
        for j in [1,2,3,4]:
            for z in [0,1,3,5,7,9,10]: # destination x coord
                if is_legal_up(cur_graph, i, j, z):
                    (new_graph, new_score) = do_move(cur_graph, i, j, z, 0)
                    states.append((new_graph, new_score+cur_score))
                    #print("appending")

    iteration+=1
    
    #if iteration == 257319:
    #for (s,sc) in states:
    #    print(f"{s}")

    
print(f"Done. Lowest score {lowest_score}")

