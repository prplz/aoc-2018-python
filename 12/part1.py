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
for _ in range(20):
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

print(sum(i + left for i, value in enumerate(field) if value))
