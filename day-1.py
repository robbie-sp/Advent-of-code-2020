import numpy as np
import pandas as pd

# Part 1 -----------------------------

data = pd.read_csv('day-1.1.txt', header=None, names=['amounts']).amounts.to_list()

for i in data:
    if 2020 - i in data:
        print(f'{i} and {2020-i} in list')
        entries = [i, 2020-i]

product = entries[0] * entries[1]

print(product)

# Part 2 -----------------------------

data = pd.read_csv('day-1.1.txt', header=None, names=['amounts']).amounts.to_list()

for i, num1 in enumerate(data):
    remainder1 = data[:i] + data[i+1:]

    for i, num2 in enumerate(remainder1):

        if num1 + num2 < 2020:

                remainder2 = data[:i] + data[i+1:]

                if 2020 - num1 - num2 in remainder2:
                    entries = [num1, num2, 2020-num1-num2]

print(entries)

product = entries[0] * entries[1] * entries[2]

print(product)
