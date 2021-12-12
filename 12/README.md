# Day 12

At first I thought I was going to hate this puzzle as I usually don't like graph traversal problems. The added twist of being able to visit some but not all nodes multiple times sounded like a lot of info to keep track of. I ended up with a working solution that simply builds lists of each path at each step, checking legality before appending to the list. It's probably not efficient in terms of memory but the dataset is small. I was afraid part 2 would grow the list enough that a brute force solution like this wouldn't work but luckily it didn't do that.

For part 2 I just had to update the code that drops the path if it would duplicate a lower case step and I added a flag to indicate that we had already done this so we don't do it again.

It turns out this problem was pretty satisfying as it wasn't overly complex but also just difficult enough that I feel accomplished having solved it