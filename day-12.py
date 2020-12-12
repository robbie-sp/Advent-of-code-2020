from typing import List
import math
import numpy as np

# Used in both parts -----------------------------

test_data = """F10
N3
F7
R90
F11"""


def move_nsew(pos: List, dir, amount):

    pos = pos.copy()

    if dir=='N':
        pos[1] += amount
    elif dir=='S':
        pos[1] -= amount
    elif dir=='E':
        pos[0] += amount
    elif dir=='W':
        pos[0] -= amount

    return pos


with open('day-12-data.txt') as f:
    nav_instructions = f.read()


# Part 1 -----------------------------

BEARING_ST = 90

def change_bearing_1(orig_bearing: int, dir, change: int):
    """calculate new bearing"""

    if dir=='L':
        change = change * -1

    new_bearing = orig_bearing + change

    if new_bearing >= 360:
        new_bearing = new_bearing - 360
    elif new_bearing < 0:
        new_bearing = 360 + new_bearing

    return new_bearing


assert(change_bearing_1(0, 'R', 90)) == 90
assert(change_bearing_1(0, 'L', 90)) == 270
assert(change_bearing_1(270, 'R', 90)) == 0
assert(change_bearing_1(180, 'L', 90)) == 90


def move_f(pos, bearing, amount):
    if bearing == 0:
        pos[1] += amount
    elif bearing == 180:
        pos[1] -= amount
    elif bearing == 90:
        pos[0] += amount
    elif bearing == 270:
        pos[0] -= amount

    return pos


def manhattan_dist_1(instructions: str, bearing: int) -> int:
    """find manhattan distance for instructions given"""

    instructions = instructions.split('\n')

    # initial conditions
    pos = [0, 0]  #( (x, y)

    for ins in instructions:
        dir = ins[0]
        amount = int(ins[1:])

        if dir in 'NSEW':
            # move based on value
            pos = move_nsew(pos, dir, amount)

        elif dir in 'LR':
            bearing = change_bearing_1(bearing, dir, amount)

        elif dir == 'F':
            pos = move_f(pos, bearing, amount)

        else:
          raise ValueError

    return abs(pos[0]) + abs(pos[1])


assert manhattan_dist_1(test_data, BEARING_ST) == 25

print(manhattan_dist_1(nav_instructions, BEARING_ST))


# Part 2 -----------------------------

WAYPOINT_ST = [10, 1]


def rotate_waypoint(waypoint, dir, amount):

    if dir=='L':
        amount = -amount

    theta = math.radians(amount)

    R = [[math.cos(theta), math.sin(theta)],
         [-math.sin(theta), math.cos(theta)]
         ]

    waypoint = np.dot(R, waypoint)

    waypoint = np.round(waypoint).astype(int)
    # length = math.sqrt(waypoint[0]^2 + waypoint[1]^2)
    # angle = math.tan(waypoint[0] / waypoint[1])


    return waypoint.tolist()


assert rotate_waypoint([10, 4], 'R', 90) == [4, -10]
assert rotate_waypoint([10, 0], 'R', 90) == [0, -10]
assert rotate_waypoint([-5, 5], 'L', 90) == [-5, -5]


def move_f_2(pos, waypoint, amount):

    new_pos = np.array(pos) + (np.array(waypoint) * amount)

    return new_pos.tolist()


assert move_f_2([0, 0], [10, 1], 10) == [100, 10]
assert move_f_2([170, 38], [4, -10], 11) == [214, -72]


def manhattan_dist_2(instructions: str, waypoint: List) -> int:
    """find manhattan distance for instructions given"""

    instructions = instructions.split('\n')

    # initial conditions
    pos = [0, 0]  #( (x, y)

    for ins in instructions:
        dir = ins[0]
        amount = int(ins[1:])

        if dir in 'NSEW':
            # move based on value
            waypoint = move_nsew(waypoint, dir, amount)

        elif dir in 'LR':
            waypoint = rotate_waypoint(waypoint, dir, amount)

        elif dir == 'F':
            pos = move_f_2(pos, waypoint, amount)

        else:
          raise ValueError

    return abs(pos[0]) + abs(pos[1])


assert manhattan_dist_2(test_data, WAYPOINT_ST) == 286

print(manhattan_dist_2(nav_instructions, WAYPOINT_ST))
