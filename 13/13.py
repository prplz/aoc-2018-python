from itertools import cycle

with open('in.txt') as f:
    lines = f.readlines()


tracks = []
carts = []


class Cart:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y
        self.turn = cycle((-1, 0, 1))

    def move(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1
        track = tracks[self.y][self.x]
        if track == '+':
            self.direction = (self.direction + next(self.turn)) % 4
        elif track == '/':
            self.direction ^= 1
        elif track == '\\':
            self.direction ^= 3

    def collides(self, other):
        return self != other and self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)


for y, line in enumerate(lines):
    tracks.append([])
    for x, char in enumerate(line):
        if char == '^':
            carts.append(Cart(0, x, y))
            tracks[y].append('|')
        elif char == '>':
            carts.append(Cart(1, x, y))
            tracks[y].append('-')
        elif char == 'v':
            tracks[y].append('|')
            carts.append(Cart(2, x, y))
        elif char == '<':
            tracks[y].append('-')
            carts.append(Cart(3, x, y))
        elif char in '\\/-|+':
            tracks[y].append(char)
        else:
            tracks[y].append(' ')

solving_part_1 = True
while True:
    for cart in sorted(carts):
        if cart not in carts:
            continue
        cart.move()
        if solving_part_1 and any(map(cart.collides, carts)):
            print(f'{cart.x},{cart.y}')
            solving_part_1 = False
        carts = [cart for cart in carts if not any(map(cart.collides, carts))]
    if len(carts) == 1:
        print(f'{carts[0].x},{carts[0].y}')
        break
