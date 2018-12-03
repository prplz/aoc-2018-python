import re
from collections import namedtuple

claim = namedtuple('claim', ('id', 'x', 'y', 'width', 'height'))

with open('in.txt') as f:
    claims = [claim(*map(int, re.findall('\d+', line))) for line in f]

for first in claims:
    for second in claims:
        if (first != second and
                second.x <= first.x + first.width and
                second.x + second.width >= first.x and
                second.y <= first.y + first.height and
                second.y + second.height >= first.y):
            break
    else:
        print(first.id)
