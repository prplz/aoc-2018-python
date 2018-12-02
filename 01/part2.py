from itertools import cycle

with open('in.txt') as f:
    series = list(map(int, f))

seen = set()
current = 0

for item in cycle(series):
    current += item
    if current in seen:
        break
    seen.add(current)

print(current)