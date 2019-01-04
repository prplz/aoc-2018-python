from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))

with open('in.txt') as f:
    points = [Point(*map(int, line.split(','))) for line in f]

min_x = min(point.x for point in points)
max_x = max(point.x for point in points)
min_y = min(point.y for point in points)
max_y = max(point.y for point in points)

print(sum(
    1
    for x in range(min_x, max_x + 1) 
    for y in range(min_y, max_y + 1)
    if sum(abs(point.x - x) + abs(point.y - y) for point in points) < 10000
))
