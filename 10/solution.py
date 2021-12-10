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


stack = []

score = 0
for row in data:
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
                if v == "}":
                    score += 1197
                if v == ")":
                    score += 3
                if v == "]":
                    score += 57
                if v == ">":
                    score += 25137
                break

print(f"Final score {score}")
