# Day 8

Part 1 was pretty easy; the hard part being the obtuse problem description. Looping through and counting the lengths was easy.

Part 2 was tricky. I could see a solution where certain digits were used to gain knowledge to figure out other digits but I didn't know how to do that algorithmically without manually working out which digits gave what information with a mess of if statements. I settled on an equally inelegant and slower solution that didn't require thinking: I generated mapping permutations until it found the correct one. It took 23.5 seconds to run the code but it worked!