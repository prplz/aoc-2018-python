with open("in.txt") as f:
    items = [*map(int, reversed(f.read().split()))]

result = 0
child_count = [1]
meta_count = []
values = [[]]
while items:
    if child_count[-1] == 0:
        child_count.pop()
        child_count[-1] -= 1
        v = values.pop()
        meta = (items.pop() for _ in range(meta_count.pop()))
        if v:
            values[-1].append(sum(v[i - 1] for i in meta if 0 < i <= len(v)))
        else:
            values[-1].append(sum(meta))
    else:
        child_count.append(items.pop())
        meta_count.append(items.pop())
        values.append([])

print(values[0][0])
