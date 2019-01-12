from itertools import count


def solve(n):
    digits = [*map(int, str(n))]
    n_digits = len(digits)
    recipes = [3, 7]
    index1 = 0
    index2 = 1

    for i in count():
        new = recipes[index1] + recipes[index2]
        if new >= 10:
            recipes.append(1)
        recipes.append(new % 10)
        index1 = (index1 + 1 + recipes[index1]) % len(recipes)
        index2 = (index2 + 1 + recipes[index2]) % len(recipes)
        if recipes[-n_digits :] == digits:
            return len(recipes) - n_digits
        if recipes[-n_digits - 1 : -1] == digits:
            return len(recipes) - n_digits - 1


print(solve(765071))
