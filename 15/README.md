# Day 15

Ooof. I do like memoization problems because they're good practice, but I implemented a standard down+right solution which was elegant but didn't work because the path could go up or left (the example solution did not do this). Part 1 was reasonable after I threw it out and used a queue to track nodes to check and a memoization table to track risks.

For part 2 this solution worked on the example but wouldn't terminate on the full dataset until I fixed a small bug. Since the memoization table can update while a node is sitting in the queue, I had to check if the node was still useful (lower risk) when it came out of the queue. At this point the code ran quickly. I forget what Dijkstra's algorithm is but I believe I inadvertantly implemented a crappier version of it.

Not my best work, but it's nice to think about this kind of problem once a year.