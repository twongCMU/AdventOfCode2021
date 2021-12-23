#Day 23

This problem was pretty straightforward. Like a previous problem, I just enumerated each possible next board state in a queue until either it was solved or there wasn't anything legal left to do. The boards were small so it ran in a reasonable amount of time. Part 2 was just a slight tweak to Part 1 and it still ran in a short amount of time due to the constrained top row

In talking with friends I'm learning that I've essentially reimplemented a worse version of Dijkstra's algorithm. There, the queue is sorted by weight (energy) so the lowest weights go first. Then when higher energy states are checked there is a greater chance that it can be pruned without processing.