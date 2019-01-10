from collections import Counter


def play(player_count, length):
    field = [0]
    current = 0
    scores = Counter()
    for i in range(0, length):
        value = i + 1
        if value % 23 == 0:
            current = (current - 7) % len(field)
            player = i % player_count + 1
            scores[player] += field.pop(current) + value
        else:
            current = (current + 2) % len(field)
            field.insert(current, value)
    [(_, winner_score)] = scores.most_common(1)
    return winner_score


print(play(466, 71436))
