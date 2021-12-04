#!/usr/bin/python3

import math
import numpy as np
import re
data = []
with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

# Brute force look for one bingo then return the sum of
# unmarked tiles
def find_bingo(boards):
    for b in boards:
        # check rows
        bingo = False
        for x in range(5):
            needed = False
            for y in range(5):
                if b[x][y] != 255:
                    needed = True
            if not needed:
                bingo = True

        for y in range(5):
            needed = False
            for x in range(5):
                if b[x][y] != 255:
                    needed = True
            if not needed:
                bingo = True

        if bingo:
            sum = 0
            for x in range(5):
                for y in range(5):
                    if b[x][y] != 255:
                        sum += b[x][y]
            return sum
    return 0

def mark_number(boards, value):
    for b in boards:
        for x in range(5):
            for y in range(5):
                if b[x][y] == value:
                    b[x][y] = 255
                    
calls = data[0].split(",")
boards = []
for i in range(1, len(data[1:]), 5):
    one_board = np.zeros((5,5),np.uint8)
    for x in range(5):
        for y in range(5):
            row = re.split('\s+', data[i+x])
            #print(f"{data[i+x]}XXXX{row}")
            one_board[x][y] = int(row[y])

    boards.append(one_board)

for c in calls:
    mark_number(boards, int(c))
    bingo_sum = find_bingo(boards)
    if bingo_sum != 0:
        print(f"Bingo! {bingo_sum * int(c)}")
        break
