# Day 14

Another dreaded grammar expansion problem. I have done enough of these to know how it goes: part 1 entices me to do a brute force solution and part 2 will raise the number of rounds high enough that brute force won't work and I have to redo it. When reading part 1 I could see a solution that wasn't brute force but I also knew it would be complex enough to hurt my ranking. I decided to do the easy out first to get part 1 done.

For part 2 I had to throw out my part 1 solution, as expected, and it was pretty fun implementing a dict to count pairs. I lost a bit of time due t a bug where, each round, I was only adding 1 to each update instead of carrying the cumulative value from the previous round. Hilariously, a friend of mine who was also stuck ended up having the exact same bug!