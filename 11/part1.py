size = 300


def make_grid(serial):
    grid = []
    for y in range(size):
        grid.append([0] * size)
        for x in range(size):
            value = x + 11
            value *= y + 1
            value += serial
            value *= x + 11
            value = value // 100 % 10
            value -= 5
            grid[y][x] = value
    return grid


grid = make_grid(1723)

positions = ((x, y) for x in range(size - 2) for y in range(size - 2))


def max_key(position):
    px, py = position
    return sum(grid[py + y][px + x] for x in range(3) for y in range(3))


x, y = max(positions, key=max_key)
print(f'{x+1},{y+1}')
