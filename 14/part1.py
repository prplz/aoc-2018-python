def solve(n):
    recipes = [3, 7]
    index1 = 0
    index2 = 1

    while len(recipes) < n + 10:
        new = recipes[index1] + recipes[index2]
        if new >= 10:
            recipes.append(1)
        recipes.append(new % 10)
        index1 = (index1 + 1 + recipes[index1]) % len(recipes)
        index2 = (index2 + 1 + recipes[index2]) % len(recipes)
    return ''.join(map(str, recipes[n : n + 10]))


print(solve(765071))
