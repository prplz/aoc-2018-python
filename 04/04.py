from collections import Counter, defaultdict

with open('in.txt') as f:
    lines = f.read().splitlines()

lines.sort()

guard_minutes = defaultdict(Counter)

for line in lines:
    command = line[19:]
    current_minute = int(line[15:17])
    if command == 'falls asleep':
        sleep_start = current_minute
    elif command == 'wakes up':
        guard_minutes[current_guard].update(range(sleep_start, current_minute))
    else:
        current_guard = int(command.split()[1][1:])


def key(item):
    guard, counter = item
    return sum(counter.values())


guard, minutes = max(guard_minutes.items(), key=key)
((minute, count),) = minutes.most_common(1)
print(guard * minute)


def key(item):
    guard, counter = item
    ((minute, count),) = counter.most_common(1)
    return count


guard, minutes = max(guard_minutes.items(), key=key)
((minute, count),) = minutes.most_common(1)
print(guard * minute)
