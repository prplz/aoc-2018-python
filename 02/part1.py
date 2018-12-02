from collections import Counter

with open('in.txt') as f:
    counters = list(map(Counter, f))

doubles = sum(2 in counter.values() for counter in counters)
tripples = sum(3 in counter.values() for counter in counters)

print(doubles * tripples)
