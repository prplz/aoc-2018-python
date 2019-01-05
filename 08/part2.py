with open("in.txt") as f:
    items = [*map(int, reversed(f.read().split()))]

result = 0
child_count = [1]
is_bottom = []
meta_count = []
values = [[]]
while items:
    if child_count[-1] == 0:
        child_count.pop()
        child_count[-1] -= 1
        if is_bottom.pop():
            values.pop()
            values[-1].append(sum(items.pop() for _ in range(meta_count.pop())))
        else:
            v = values.pop()
            indices = [items.pop() for _ in range(meta_count.pop())]
            values[-1].append(sum(v[i - 1] for i in indices if 0 < i <= len(v)))
    else:
        child_count.append(items.pop())
        is_bottom.append(child_count[-1] == 0)
        meta_count.append(items.pop())
        values.append([])

print(values[0][0])
