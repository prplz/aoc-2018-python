import re
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    dx: int
    dy: int


with open('in.txt') as f:
    points = [Point(*map(int, re.findall(r'-?\d+', line))) for line in f]

dist = 9e9
frame = 0
while True:
    for point in points:
        point.x += point.dx
        point.y += point.dy
    x = sum(point.x for point in points) // len(points)
    y = sum(point.y for point in points) // len(points)
    new_dist = sum(abs(x - point.x) + abs(y - point.y) for point in points)
    if new_dist > dist:
        for point in points:
            point.x -= point.dx
            point.y -= point.dy
        for y in range(y - 10, y + 10):
            print(
                ''.join(
                    '#'
                    if any(point.y == y and point.x == x for point in points)
                    else '.'
                    for x in range(x - 50, x + 50)
                )
            )
        print(frame)
        break
    dist = new_dist
    frame += 1
