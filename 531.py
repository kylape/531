#!/usr/bin/python3

COLUMN_WIDTH = 12
SEPARATOR = "+%s+" % "+".join("-" * COLUMN_WIDTH for i in range(8))

WORKING_MAX_PCT = 0.9

# Each tuple represents one week
# Each inner tuple represents one set
# The two items in each tuple are "percent weight of working max"
# and "number of reps"
PROGRAM = (
    ((0.65, 5), (0.75, 5), (0.85, 5)),
    ((0.70, 3), (0.80, 3), (0.90, 3)),
    ((0.75, 5), (0.85, 3), (0.95, 1)),
    ((0.40, 5), (0.50, 5), (0.60, 5))
)

BBB_SETS = [[(0.35, 10) for i in range(5)] for i in range(4)]

ASSISTANCE = (
    ((0.50, 10), (0.60, 10), (0.70, 10)),
    ((0.60,  8), (0.70,  8), (0.80,  6)),
    ((0.65,  5), (0.75,  5), (0.85,  5)),
    ((0.40,  5), (0.50,  5), (0.60,  5))
)

main_lifts = ("press", "deadlift", "bench", "squat")
assistance_lifts = ("row", "front squat", "dips", "shrug")

main_maxes = [m * WORKING_MAX_PCT for m in (130, 275, 200, 250)]
assistance_maxes = [m * WORKING_MAX_PCT for m in (175, 150, 35, 175)]


def format_row(data):
    return "|%s|" % "|".join(k.center(COLUMN_WIDTH) for k in data)


def round_weight(w):
    remainder = w % 2.5
    if remainder < 1.25:
        return w - remainder
    else:
        return w + (2.5 - remainder)


def format_set(weight, reps):
    final_weight = max([round_weight(weight), 45.0])
    return "%s x %s" % (str("%.1f" % final_weight).rjust(5), str(reps).rjust(2))


for i, week in enumerate(PROGRAM):
    print(("Week %d" % (i+1)).center(len(SEPARATOR)))
    print(SEPARATOR)
    print(format_row(lift.upper() for lift in main_lifts + assistance_lifts))
    print(SEPARATOR)
    for pct_max, reps in PROGRAM[i]:
        sets = [format_set(w * pct_max, reps) for w in main_maxes]
        sets.extend(format_set(w * pct_max, reps) for w in assistance_maxes)
        print(format_row(sets))
    for pct_max, reps in BBB_SETS[i]:
        sets = [format_set(w * pct_max, reps) for w in main_maxes]
        sets.extend(" " * 12 for i in range(4))
        print(format_row(sets))
    print(SEPARATOR)
    print()
