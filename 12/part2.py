import re

initial_input = '#.####...##..#....#####.##.......##.#..###.#####.###.##.###.###.#...#...##.#.##.#...#..#.##..##.#.##'

rules_input = """.##.. => .
..##. => #
.#..# => #
.#.#. => .
..#.. => #
###.. => #
##..# => .
##... => #
#.### => #
.##.# => #
#.... => .
###.# => .
..... => .
.#... => #
....# => .
#.#.. => .
...#. => #
#...# => .
##.#. => .
.#.## => #
..#.# => #
#.#.# => .
.#### => .
##### => .
..### => .
...## => .
#..## => .
#.##. => .
#..#. => #
.###. => #
##.## => #
####. => ."""

field = [c == '#' for c in initial_input]

rules = {}
for line in rules_input.split('\n'):
    m = [c == '#' for c in re.findall('[.#]', line)]
    rules[tuple(m[:5])] = m[5]

left = 0
previous = 0
for i in range(1000):
    while field[:3] != [False, False, False]:
        field.insert(0, False)
        left -= 1
    while field[-3:] != [False, False, False]:
        field.append(False)
    field = [
        rules.get(tuple(field[i - 2 : i + 3]), False)
        for i in range(len(field))
    ]
    # print(''.join('.#'[v] for v in field))
    current = sum(i + left for i, value in enumerate(field) if value)
    diff = current - previous
    previous = current

print(current + (50000000000 - 1000) * diff)
