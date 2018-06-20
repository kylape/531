# 5/3/1 Program Calculator

Print calculations for each set for an entire 5/3/1 cycle.

Output for the first week week using BBB as a supplemental program:

```
                        Week 1
+------------+------------+------------+------------+
|   PRESS    |  DEADLIFT  |   BENCH    |   SQUAT    |
+------------+------------+------------+------------+
|  87.5 x  5 | 207.5 x  5 | 135.0 x  5 | 190.0 x  5 |
| 102.5 x  5 | 240.0 x  5 | 155.0 x  5 | 220.0 x  5 |
| 115.0 x  5 | 272.5 x  5 | 175.0 x  5 | 247.5 x  5 |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |
+------------+------------+------------+------------+
```

Accessory exercises can be added as well:

```
                                                  Week 1
+------------+------------+------------+------------+------------+------------+------------+------------+
|   PRESS    |  DEADLIFT  |   BENCH    |   SQUAT    |   SHRUG    |FRONT SQUAT |    DIPS    |    ROW     |
+------------+------------+------------+------------+------------+------------+------------+------------+
|  87.5 x  5 | 207.5 x  5 | 135.0 x  5 | 190.0 x  5 | 122.5 x 10 | 107.5 x 10 |  45.0 x 10 | 100.0 x 10 |
| 102.5 x  5 | 240.0 x  5 | 155.0 x  5 | 220.0 x  5 | 145.0 x 10 | 130.0 x 10 |  47.5 x 10 | 120.0 x 10 |
| 115.0 x  5 | 272.5 x  5 | 175.0 x  5 | 247.5 x  5 | 170.0 x 10 | 150.0 x 10 |  57.5 x 10 | 137.5 x 10 |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |            |            |            |            |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |            |            |            |            |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |            |            |            |            |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |            |            |            |            |
|  75.0 x 10 | 175.0 x 10 | 115.0 x 10 | 160.0 x 10 |            |            |            |            |
+------------+------------+------------+------------+------------+------------+------------+------------+
```

## Configuration
Configuration is managed from within `lifts.ini`.  There are three sections:

### `training_max_pct`
This is the multiplier used to calculate your training max.  If you want the same training max percentage to be applied to all lifts, only add a `default` key, e.g.:

    default=0.9

If you want to customize the training max for a particular lift, add a value for that lift:

    press=0.85

### `maxes`
Define the real 1RM for each of your lifts here.  Example:

    press=150

### `lifts`
Define all the lifts or exercises to include in your current cycle.  The key is the name of the lift, and the value is the program(s) to apply.  Example:

    press=five_three_one,boring_but_big

This will add the press using the typical 5/3/1 program appended with the supplemental BBB program.  Each lift needs to have its own program listed in this section, e.g.:

    press=five_three_one,boring_but_big
    deadlift=five_three_one,boring_but_big
    bench=five_three_one,boring_but_big
    squat=five_three_one,boring_but_big

The following programs are currently available:

- five_three_one
- boring_but_big
- first_set_last
- assistance
- training_max_test

More can be added by creating a Python function with the desired name of the program as the function name in the python script.

## Execution

Simply run `./531.py`.  Requires Python 3.
