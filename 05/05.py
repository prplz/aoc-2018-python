import string

with open('in.txt') as f:
    polymer = list(f.read())


def react(polymer):
    polymer = list(polymer)
    removed_any = True

    while removed_any:
        removed_any = False
        for i in reversed(range(len(polymer))):
            if i < len(polymer) - 1:
                current = polymer[i]
                previous = polymer[i + 1]
                if current != previous and current.lower() == previous.lower():
                    polymer.pop(i + 1)
                    polymer.pop(i)
                    removed_any = True

    return polymer


print(len(react(polymer)))


def react_without_letter(polymer, letter):
    lower_and_upper = letter.lower(), letter.upper()
    return react(p for p in polymer if p not in lower_and_upper)


reacted_lengths = (len(react_without_letter(polymer, letter)) for letter in string.ascii_lowercase)

print(min(*reacted_lengths))
