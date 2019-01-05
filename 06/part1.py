from collections import Counter, namedtuple
from operator import itemgetter

Point = namedtuple('Point', ('x', 'y'))

with open('in.txt') as f:
    points = [Point(*map(int, line.split(','))) for line in f]

min_x = min(point.x for point in points)
max_x = max(point.x for point in points)
min_y = min(point.y for point in points)
max_y = max(point.y for point in points)

counter = Counter()
infinite = set()

for x in range(min_x - 1, max_x + 2):
    for y in range(min_y - 1, max_y + 2):
        distances = [(point, abs(point.x - x) + abs(point.y - y)) for point in points]
        best, best_distance = min(distances, key=itemgetter(1))
        if best in infinite:
            continue
        if not (min_x <= x <= max_x and min_y <= y <= max_y):
            infinite.add(best)
            counter.pop(best, None)
            continue
        if all(
            distance > best_distance for point, distance in distances if point != best
        ):
            counter[best] += 1

print(counter.most_common(1)[0][1])
