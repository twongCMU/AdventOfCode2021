# Day 5

I was less enthusiastic about this one. I don't know good tricks for manipulating rows and columns
of a matrix much less diagonals. Luckily this problem doesn't require the full matrix to be stored
so I used a dict to store visited coordinates.

Since the ranges are not necessarily in increasing order I got really hacky
trying to figure out increasing and decreasing. Part 1 came fairly easily but in part 2 I got
bogged down figuring out how to increase and decrease two separate axes at once so it was very
buggy and got more and more hacky. I'm kind of embarrassed by my solution for part 2. I probably
should have deleted the diagonals code and started over once it started getting worse and worse
