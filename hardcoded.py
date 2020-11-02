#!/usr/local/bin/python3
#%%
from datetime import datetime, timedelta

PLAYER_LIST = ['Arun', 'Murali', 'RamIyer', 'Ramu', 'Sri', 'Vish']
PLAYERS = set(PLAYER_LIST)
NUM_WEEKS=24
#%%
d = datetime.today()
t = timedelta((12 - d.weekday()) % 7)
d += t
# print(f"{d:%Y/%m/%d}")
dates = [d+timedelta(i*7) for i in range(NUM_WEEKS)]
dates

#%%
byes = [ {PLAYER_LIST[int(i[0]) - 1], PLAYER_LIST[int(i[1]) - 1]} for i in
"""
24
35
46
23
14
36
15
26
34
12
56
13
45
16
25
---------
34
12
56
23
45
16
----------
25
14
36
""".split("\n") if len(i) == 2 ]
players = [sorted(list(PLAYERS - b)) for b in byes]
schedule = zip(dates, players)
for dt, (a,b,c,d) in schedule:
    resting = list(sorted(PLAYERS - set((a,b,c,d))))
    print(f"{dt:%Y-%m-%d},{a},{b},{c},{d},", ",".join(resting))

# %%
