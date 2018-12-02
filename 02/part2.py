from itertools import combinations

with open('in.txt') as f:
    ids = f.read().splitlines()

for first, second in combinations(ids, 2):
    if sum(a != b for a, b in zip(first, second)) == 1:
        print(''.join(a for a, b in zip(first, second) if a == b))
