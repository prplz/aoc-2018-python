with open("in.txt") as f:
    items = [*map(int, reversed(f.read().split()))]

result = 0
child_count = [1]
meta_count = []
while items:
    if child_count[-1] == 0:
        child_count.pop()
        child_count[-1] -= 1
        result += sum(items.pop() for _ in range(meta_count.pop()))
    else:
        child_count.append(items.pop())
        meta_count.append(items.pop())

print(result)
