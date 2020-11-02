## Tennis scheduling
Six people share a winter tennis contract that allows four of them them to play each Saturday morning for 30 weeks

Make a fair schedule such that
1. Every combination of 4 players is evenly represented
1. Everyone plays the same number of times
1. No one sits out on consecutive days.

1. The first condition can be met enumerating all combinations of 4 people (6C4 = 15) and repeating them as necessary. If the number of weeks is not a multiple of 15, some combinations will occur 1 more time than the rest.

2. The second condition is also tricky if N is not a multiple of 15. But it can be achieved for any multiple of 3 weeks

3. The only non brute force solution is a kind of heuristic that mostly works, involving brute force for a few remaining cases.



