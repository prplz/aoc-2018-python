import re
from collections import Counter
from itertools import product

usages = Counter()

with open('in.txt') as f:
    for line in f:
        id_, x, y, width, height = map(int, re.findall('\d+', line))
        usages.update(product(range(x, x + width), range(y, y + height)))

print(sum(value > 1 for value in usages.values()))
