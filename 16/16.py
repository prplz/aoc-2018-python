import re

opcodes = (
    'addr',
    'addi',
    'mulr',
    'muli',
    'banr',
    'bani',
    'borr',
    'bori',
    'setr',
    'seti',
    'gtir',
    'gtri',
    'gtrr',
    'eqir',
    'eqri',
    'eqrr',
)


def process(opcode, args, registers):
    def set_register(index, value):
        return tuple(
            value if i == index else r for i, r in enumerate(registers)
        )

    a, b, c = args
    if opcode == 'addr':
        return set_register(c, registers[a] + registers[b])
    if opcode == 'addi':
        return set_register(c, registers[a] + b)
    if opcode == 'mulr':
        return set_register(c, registers[a] * registers[b])
    if opcode == 'muli':
        return set_register(c, registers[a] * b)
    if opcode == 'banr':
        return set_register(c, registers[a] & registers[b])
    if opcode == 'bani':
        return set_register(c, registers[a] & b)
    if opcode == 'borr':
        return set_register(c, registers[a] | registers[b])
    if opcode == 'bori':
        return set_register(c, registers[a] | b)
    if opcode == 'setr':
        return set_register(c, registers[a])
    if opcode == 'seti':
        return set_register(c, a)
    if opcode == 'gtir':
        return set_register(c, int(a > registers[b]))
    if opcode == 'gtri':
        return set_register(c, int(registers[a] > b))
    if opcode == 'gtrr':
        return set_register(c, int(registers[a] > registers[b]))
    if opcode == 'eqir':
        return set_register(c, int(a == registers[b]))
    if opcode == 'eqri':
        return set_register(c, int(registers[a] == b))
    if opcode == 'eqrr':
        return set_register(c, int(registers[a] == registers[b]))


def read_ints(s):
    return tuple(map(int, re.findall(r'\d+', s)))


def read_samples(lines):
    lines_iter = iter(lines)
    while True:
        before = next(lines_iter)
        args = next(lines_iter)
        after = next(lines_iter)
        if before == '' and args == '':
            return
        yield read_ints(before), read_ints(args), read_ints(after)
        next(lines_iter)


def read_program(lines):
    lines_iter = iter(lines)
    previous = None
    for line in lines_iter:
        if line == '' and previous == '':
            break
        previous = line
    next(lines_iter)
    yield from map(read_ints, lines_iter)


with open('in.txt') as f:
    lines = [line.rstrip() for line in f]


# part 1
print(
    sum(
        sum(process(opcode, args[1:], before) == after for opcode in opcodes)
        >= 3
        for before, args, after in read_samples(lines)
    )
)

# part 2
opcode_table = [None] * 16
for before, args, after in read_samples(lines):
    if opcode_table[args[0]]:
        continue
    candidates = [
        opcode
        for opcode in opcodes
        if opcode not in opcode_table
        and process(opcode, args[1:], before) == after
    ]
    if len(candidates) == 1:
        opcode, = candidates
        opcode_table[args[0]] = opcode
registers = (0, 0, 0, 0)
for line in read_program(lines):
    registers = process(opcode_table[line[0]], line[1:], registers)
print(registers[0])
