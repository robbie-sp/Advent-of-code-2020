"""day 13

missing a trick on the second part. Must be a way to reduce number
of times tried our to hold calcs in memory to make process faster

part 2 didn't finish after an hour.

error was in stepping through times rather than by buses. Lots of good solns online.
"""


from typing import List

# test data
test_data = """939
7,13,x,x,59,x,31,19
"""

def prepare_data(raw_data: str):
    data = raw_data.split('\n')
    earliest_time = int(data[0])
    bus_ids = [int(id) for id in data[1].split(',') if id != 'x']

    return earliest_time, bus_ids

def find_earliest_bus(raw_data, max_time=1e5):

    earliest_time, bus_ids = prepare_data(raw_data)

    time = earliest_time

    while time < max_time:
        for id in bus_ids:
            if time % id == 0:
                return (time - earliest_time) * id
        else:
            time += 1

    raise ArithmeticError(f'max time reached')


assert find_earliest_bus(test_data) == 295


with open('day-13-data.txt') as f:
    data = f.read()

    print(find_earliest_bus(data, max_time=1e8))



# def first_timestamp(data: str, max_time=1e8, start_time:int=0):
#     bus_ids = data.split(',')

#     bus_ids_ints = []  # better done wih list comprehension
#     for id in bus_ids:
#         if id != 'x':
#             bus_ids_ints.append(int(id))
#         else:
#             bus_ids_ints.append(id)

#     time = start_time

#     num_buses = len(bus_ids_ints)

#     not_solved = True

#     while not_solved and time < max_time:
#         time += bus_ids_ints[0]

#         for index, id in enumerate(bus_ids_ints):
#             if id == 'x':
#                 continue  # move to next bus
#             elif (time + index) % id != 0:
#                 break  # if next bus doesn't meet condition go next possible start point
#             elif index + 1 == num_buses:
#                 not_solved = False

#     return time


def first_timestamp(data: str, max_time=1e8, start_time:int=0):
    bus_ids = data.split(',')

    buses = [(index, int(id)) for index, id in enumerate(bus_ids) if id !='x']

    sorted_buses = sorted(buses, key=lambda tup: tup[1], reverse=True)

    num_buses = len(sorted_buses)

    not_solved = True
    if start_time:
        time = start_time
    else:
        time = (sorted_buses[0][1] - sorted_buses[0][0])

    while not_solved and time < max_time:

        for counted, (index, id) in enumerate(sorted_buses):
            if (time + index) % id != 0:
                break  # if next bus doesn't meet condition go next possible start point
            elif counted + 1 == num_buses:
                not_solved = False
                return time

        time += sorted_buses[0][1]



# first_timestamp('17,x,13,19', start_time=3417)

#assert first_timestamp(test_data.split('\n')[1], start_time=test_start_time) == 1068781
assert first_timestamp('17,x,13,19', max_time=3500) == 3417
assert first_timestamp('67,7,59,61') == 754018
assert first_timestamp('67,x,7,59,61') == 779210
assert first_timestamp('67,7,x,59,61') == 1261476
assert first_timestamp('1789,37,47,1889', max_time=1e10) == 1202161486

# 100_000_000_000_000

with open('day-13-data.txt') as f:
    data = f.read()

    earliest_time = first_timestamp(data.split('\n')[1], max_time=1e15)

    print(earliest_time)