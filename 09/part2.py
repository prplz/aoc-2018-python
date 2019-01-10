from collections import Counter, namedtuple


class Node:
    __slots__ = ('value', 'previous', 'next')

    def forward(self, n):
        current = self
        for _ in range(n):
            current = current.next
        return current

    def back(self, n):
        current = self
        for _ in range(n):
            current = current.previous
        return current

    def remove(self):
        res = self.next
        self.previous.next = self.next
        self.next.previous = self.previous
        self.next = None
        self.previous = None
        return res

    def insert(self, value):
        new = Node()
        new.value = value
        new.next = self
        new.previous = self.previous
        self.previous.next = new
        self.previous = new
        return new


def play(player_count, length):
    current = Node()
    current.value = 0
    current.next = current
    current.previous = current
    scores = Counter()
    for i in range(0, length):
        value = i + 1
        if value % 23 == 0:
            current = current.back(7)
            player = i % player_count + 1
            scores[player] += current.value + value
            current = current.remove()
        else:
            current = current.forward(2).insert(value)
    [(_, winner_score)] = scores.most_common(1)
    return winner_score


print(play(466, 7143600))
