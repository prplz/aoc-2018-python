size = 300


def make_grid(serial):
    grid = [0] * size * size
    for y in range(size):
        for x in range(size):
            value = x + 11
            value *= y + 1
            value += serial
            value *= x + 11
            value = value // 100 % 10
            value -= 5
            grid[x + y * size] = value
    return grid


def power_generator(serial):
    grid = make_grid(serial)
    for x in range(size):
        for y in range(size):
            power = grid[x + y * size]
            yield (x, y, 0, power)
            for s in range(1, size - max(x, y)):
                for i in range(s):
                    power += grid[x + i + (y + s) * size]
                    power += grid[x + s + (y + i) * size]
                power += grid[x + s + (y + s) * size]
                if power > 0:
                    yield (x, y, s, power)
                elif s > 6:
                    # assume that over a certain size and 0 or less power will
                    # not reach a solution.
                    # using a lower number is faster, but can miss solutions
                    break


def solve(serial):
    x, y, s, _ = max(power_generator(serial), key=lambda x: x[3])
    return f'{x+1},{y+1},{s+1}'


print(solve(1723))
