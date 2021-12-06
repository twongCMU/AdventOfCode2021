# Day 6

Another fun one. Part one I just brute forced it and added new fish to the end
of the array. I placed 116th which is a new personal best! I was 5 seconds away from making it
onto the leaderboard. I didn't expect to do better than my 180th place last year so it was a
pleasant result even if I didn't get any top-100 points for it.

Part 2 could not be brute forced. I spent some time trying to think of the math required
to compute how many fish a single fish would spawn at a certain round number then realized
it would be easier to just track categories of fish. Fish can be in only one of 9 situations
being the number of days until spawn so we only need to check and update 9 elements each round
and can count how many of each fish are at that stage.

