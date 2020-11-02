#!/usr/local/bin/python3
#%%
import itertools as it
import random
from datetime import datetime, timedelta

#%%
PLAYERS = set(['Arun', 'Murali', 'RamIyer', 'Ramu', 'Sri', 'Vish'])
# start with this
FIRST_LINEUP = set(['Arun', 'RamIyer', 'Sri', 'Vish'])
NUM_WEEKS=24
NUM_SLOTS=4
NUM_STANDBYES = len(PLAYERS) - NUM_SLOTS

def no_repeating_off_day(l1, l2):
    standbyes = (PLAYERS - set(l1)) | (PLAYERS - set(l2))
    return len(standbyes) == 2 * NUM_STANDBYES

def insert_without_repeating_off_day(new_lineup, schedule):
    for i in range(1,len(schedule)):
        if (
            (i == 0 or no_repeating_off_day(schedule[i-1], new_lineup)) and
            (i >= len(schedule) or no_repeating_off_day(schedule[i], new_lineup)) 
        ):
            schedule.insert(i, new_lineup)
            return
    print("Couldn't find a place for", new_lineup, "appending at end")
    schedule.append(new_lineup)

def print_sched(sched):
    for i,t in enumerate(sched): print(i+1, t)


#%%
d = datetime.today()
t = timedelta((12 - d.weekday()) % 7)
d += t
# print(f"{d:%Y/%m/%d}")
dates = [d+timedelta(i*7) for i in range(NUM_WEEKS)]
dates
#%%
byes = sorted([sorted(l) for l in it.combinations(PLAYERS, 2)])
byes

#%%
tentative_schedule = [set(l) for l in it.combinations(PLAYERS, 4)]
print("Order:")
print_sched(tentative_schedule)
n_cycles = round(NUM_WEEKS / len(tentative_schedule) + 0.5)
tentative_schedule *= n_cycles
tentative_schedule = tentative_schedule[:NUM_WEEKS]
print("Tentative full schedule:")
print_sched(tentative_schedule)
i = next((i for i,v in enumerate(tentative_schedule) if set(v) == FIRST_LINEUP), -1)
print(i)
tentative_schedule = tentative_schedule[i:] + tentative_schedule[:i]

standbyes = [list(PLAYERS - set(ts)) for ts in tentative_schedule]
#standbyes[:-1][::2] + standbyes[1:][::2]

# %%
final_schedule=[tentative_schedule[0]]
remaining = tentative_schedule[1:]
prev_standbyes = PLAYERS - set(final_schedule[0])

outer_cnt = inner_cnt = 0
print(1, final_schedule[0], prev_standbyes)
difficult_cases = 0

while remaining:
    outer_cnt += 1
    lineup = remaining.pop(0)
    standbyes = PLAYERS - set(lineup)
    tries = 1
    while prev_standbyes & standbyes and tries <= len(remaining):
        #print("dbg", len(final_schedule), tries)
        tries += 1
        inner_cnt += 1
        # same person sitting out as in prev week
        remaining.append(lineup)
        lineup = remaining.pop(0)
        standbyes = PLAYERS - set(lineup)
    if prev_standbyes & standbyes:
        insert_without_repeating_off_day(lineup, final_schedule)
        difficult_cases += 1
    else:
        final_schedule.append(lineup)
        print(len(final_schedule), lineup, standbyes)
        prev_standbyes = standbyes

print(outer_cnt, inner_cnt, difficult_cases)
for dt, (a,b,c,d) in zip(dates, final_schedule):
    resting = list(sorted(PLAYERS - set((a,b,c,d))))
    print(f"{dt:%Y-%m-%d},{a},{b},{c},{d},", ",".join(resting))

# %%
