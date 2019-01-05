from collections import defaultdict, namedtuple

requirements = defaultdict(set)
chars = set()

with open('in.txt') as f:
    for line in f:
        split = line.split()
        before = split[1]
        after = split[7]
        chars.add(before)
        chars.add(after)
        requirements[after].add(before)

result = ''
remaining = set(chars)

while remaining:
    next_char = min(char for char in remaining if requirements[char] <= set(result))
    result += next_char
    remaining.remove(next_char)

print(result)

Worker = namedtuple('Worker', ('char', 'finish_time'))

result = ''
remaining = set(chars)
workers = [None] * 5
time = 0


def work_time(char):
    return 61 + ord(char) - ord('A')


while True:
    for i, worker in enumerate(workers):
        if worker is not None and worker.finish_time == time:
            result += worker.char
            workers[i] = None
    for i, worker in enumerate(workers):
        if worker is None:
            next_char = min(
                (char for char in remaining if requirements[char] <= set(result)),
                default=None,
            )
            if next_char:
                remaining.remove(next_char)
                workers[i] = Worker(next_char, time + work_time(next_char))
    if not any(workers):
        break
    time += 1

print(time)
