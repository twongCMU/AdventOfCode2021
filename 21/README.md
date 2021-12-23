# Day 21

Once again, a relatively easy part 1 plagued by bugs. I must have fixed 20 bugs before I got my code working. I also made silly errors like forgetting that the dice only goes up to 100.

Part 2 was somewhat fun. The problem seemed impossible at the start and I was looking for some kind of mathematical formula that would help. As I was coding what I thought would work I stumbled upon an actual solution which was to just keep track of how many times I see a certain state and process them all as a batch (much like the number of fish problem from earlier in this AoC). I have an inefficient O(n) lookup in the code that I'm too lazy to fix since the code still produces an answer in under a minute. It was satisfying to be able to solve the problem in under 2 hours even though I had to work out a solution for part 2.