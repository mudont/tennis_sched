## Tennis scheduling problem

Six friends share a winter tennis contract that allows any four of them them to play each Saturday morning for 30 weeks
```
NUM_WEEKS=30
GROUP_SIZE=6
NUM_PLAYERS_ON_COURT=4
```

Make a fair schedule such that
1. Every combination of 4 players is represented evenly
1. Everyone plays the same number of times
1. No one sits out on consecutive days.

## Notes
1. The first condition can be met enumerating all combinations of 4 people (6C4 = 15) and repeating them as necessary. If the number of weeks is not a multiple of 15, some combinations will occur 1 more time than the rest.

2. The second condition is also tricky if N is not a multiple of 15. But it *can* be achieved for any multiple of 3 weeks. 

3. The only non brute force solution I know is a heuristic that mostly works, involving brute force for a few remaining cases. 

4. The interesting thing is condition #3 is easy to meet if we sacrifice the first condition that every combination be evenly represented. For example, We can have a simple round robin schedule where 1,2 sit out on week one, 3,4 on week two, 5,6 on week three, 1,2 again on week 4,....

