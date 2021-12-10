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



incomplete = []
for row in data:
    stack = []    
    corrupted = False
    for v in row:
        if v == "{" or v == "(" or v == "[" or v == "<":
            print(f"append {v}")
            stack.append(v)
        else:
            pair = ""
            if v == ")":
                pair = "("
            if v == "}":
                pair = "{"
            if v == ">":
                pair = "<"
            if v == "]":
                pair = "["
                
            if stack[-1] == pair:
                print(f"pop for {v} {stack[-1]}")
                stack.pop(-1)
            else:
                print(f"Mismatched {v} {stack[-1]}")
                corrupted = True
                break
    if not corrupted:
        incomplete.append(stack)

scores = []
for row in incomplete:
    row_rev = row[::-1]
    score=0

    for i, v in enumerate(row_rev):
        score *=5
        if v == "(":
            score+=1
        if v == "{":
            score+=3
        if v == "<":
            score+=4
        if v == "[":
            score+=2
    scores.append(score)
scores.sort()
print(f"Final score {scores} {len(scores)} {scores[int(len(scores)/2)]}")
