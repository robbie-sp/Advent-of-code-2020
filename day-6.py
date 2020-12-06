test_data = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""

# Part 1 -----------------------------

def sum_of_counts(answers: str) -> int:
    groups = []
    count = 0

    lines = answers.split('\n')

    yeses = set()

    for l in lines:
        if l == '':
            groups.append(len(yeses))
            count += len(yeses)
            yeses = set()

        for q in l:
            yeses.add(q)

    print(groups)

    return count


assert sum_of_counts(test_data) == 11


with open('day-2-data.txt') as f:
    text = f.read()
    print(sum_of_counts(text))

# Part 2 -----------------------------

from collections import Counter

def sum_of_counts_all(answers: str) -> int:
    groups = []
    count = 0

    lines = answers.split('\n')

    yeses = Counter()
    num_passengers = 0

    for l in lines:
        if l == '':

            # results for group
            same_ans = [x for x in yeses if yeses[x] == num_passengers]
            groups.append(len(same_ans))

            # reset
            yeses = Counter()
            num_passengers = 0

        for q in l:
            yeses.update(q)

        if l != '':
            num_passengers +=1


    print(groups)

    return sum(groups)

assert sum_of_counts_all(test_data) == 6

with open('day-2-data.txt') as f:
    text = f.read()
    print(sum_of_counts_all(text))
