#!/usr/bin/python3

import math
import numpy as np
import re

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
from stack import Stack
data = []
import itertools

with open("input") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)

# explode test cases
tests = ["[[[[[9,8],1],2],3],4]",
         "[7,[6,[5,[4,[3,2]]]]]",
         "[[6,[5,[4,[3,2]]]],1]",
         "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
         "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"]
ans = ["[[[[0,9],2],3],4]",
       "[7,[6,[5,[7,0]]]]",
       "[[6,[5,[7,0]]],3]",
       "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
       "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"]
for i, v in enumerate(tests):
    s = Stack()
    s.create(v)
    s.explode()
    res = s.get_string()
    assert res == ans[i], f"Got {res} expected {ans[i]}"


def reduce_string(string):
    s = Stack()
    s.create(string)
    
    action_taken = True
    while action_taken:
        action_taken = False

        if s.explode():
            action_taken = True
            continue

        if s.split_num():
            action_taken = True
            continue

    res_string = s.get_string()
    value = s.compute_sum()
    return (res_string, value)

def add_two(a, b):
    return f"[{a},{b}]"

# full test case
foo = add_two("[[[[4,3],4],4],[7,[[8,4],9]]]","[1,1]")
good_res = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
(res, value) = reduce_string(foo)
assert res == good_res , f"Got {res} expected {good_res}"


cur_string = data[0]
for i in range(1, len(data)):
    cur_string = add_two(cur_string, data[i])
    (cur_string, value) = reduce_string(cur_string)

print(f"Part 1 string {cur_string} and value {value}")
values = []
for (a, b) in itertools.permutations(data, 2):
    foo = add_two(a, b)
    (res, v) = reduce_string(foo)
    values.append(v)
print(f"Part 2 {max(values)}")

