#!/usr/bin/env python3
import configparser
from collections import OrderedDict
from itertools import chain

COLUMN_WIDTH = 12

# Each tuple represents one week
# Each inner tuple represents one set
# The two items in each tuple are "percent weight of working max"
# and "number of reps"


def five_three_one():
    return (
        ((0.65, 5), (0.75, 5), (0.85, 5)),
        ((0.70, 3), (0.80, 3), (0.90, 3)),
        ((0.75, 5), (0.85, 3), (0.95, 1)),
        ((0.40, 5), (0.50, 5), (0.60, 5))
    )


def boring_but_big():
    return [[(0.55, 10) for i in range(5)] for i in range(4)]


def first_set_last():
    return [[(i, 5) for k in range(5)] for i in (0.65, 0.70, 0.75, 0.40)]


def accessory():
    return (
        ((0.50, 10), (0.60, 10), (0.70, 10)),
        ((0.60, 8), (0.70, 8), (0.80, 6)),
        ((0.65, 5), (0.75, 5), (0.85, 5)),
        ((0.40, 5), (0.50, 5), (0.60, 5))
    )


def training_max_test():
    return [((0.70, 5), (0.80, 5), (0.90, 5), (1.00, 5))]


p_cache = {}


def get_program(p):
    if p not in p_cache:
        p_cache[p] = globals()[p]()
    return p_cache[p]


def separator(column_cnt):
    return "+%s+" % "+".join("-" * COLUMN_WIDTH for i in range(column_cnt))


def format_row(data):
    return "|%s|" % "|".join(k.center(COLUMN_WIDTH) for k in data)


def round_weight(w):
    remainder = w % 2.5
    if remainder < 1.25:
        return w - remainder
    else:
        return w + (2.5 - remainder)


def fill_out_lifts(lifts):
    """Add empty sets to the end of a lift to make set length equal"""
    mx_len = max(len(l) for l in lifts)
    for lift in lifts:
        lift.extend("" for _ in range(mx_len - len(lift)))


def format_set(weight, reps):
    final_weight = max([round_weight(weight), 45.0])
    return "%s x %s" % (str("%.1f" % final_weight).rjust(5), str(reps).rjust(2))


def parse_config():
    config = configparser.ConfigParser()
    config.read("lifts.ini")
    lifts = OrderedDict()

    for lift in (l.strip() for l in config["lifts"]):
        programs = [l.strip() for l in config["lifts"][lift].split(",")]
        lifts[lift] = programs

    maxes = {lift: float(config["maxes"][lift].strip()) for lift in config["maxes"]}
    training_max_pcts = {lift: float(config["training_max_pct"][lift].strip())
                         for lift in config["training_max_pct"]}

    default_max_pct = training_max_pcts.get("default", 0.9)

    training_maxes = {}
    for lift, mx in maxes.items():
        training_maxes[lift] = mx * training_max_pcts.get(lift, default_max_pct)

    return lifts, maxes, training_maxes


def print_plan(lifts, maxes):
    programs = set(chain.from_iterable(lifts.values()))
    week_cnt = max(len(get_program(p)) for p in programs)
    SEP = separator(len(lifts))
    for week in range(week_cnt):
        print(("Week %d" % (week + 1)).center(len(SEP)))
        print(SEP)
        print(format_row(lift.upper() for lift in lifts))
        print(SEP)
        lifts_sets = []
        for lift, programs in lifts.items():
            lift_mx = maxes[lift]
            lift_sets = []
            for program in (get_program(p)[week] for p in programs):
                lift_sets.extend(format_set(lift_mx * pct, rep) for pct, rep in program)
            lifts_sets.append(lift_sets)
        fill_out_lifts(lifts_sets)
        for row in zip(*lifts_sets):
            print(format_row(row))
        print(SEP)
        print()


def print_maxes(maxes, training_maxes):
    print("Current lift maxes")
    lift_col_size = max(len(l) for l in maxes)
    for lift, mx in maxes.items():
        trng_mx = training_maxes[lift]
        trng_pct = trng_mx / mx
        print("%s %s @ %.2f%%" % (lift.ljust(lift_col_size),
                                  str(round_weight(mx)).zfill(5),
                                  trng_pct))


if __name__ == "__main__":
    lifts, maxes, training_maxes = parse_config()
    print_plan(lifts, training_maxes)
    print_maxes(maxes, training_maxes)
