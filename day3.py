import math
import re

text = list(open('inputTxt/day3input.txt'))

board = {(x, y) : [] for x in range(140) for y in range(140) if text[x][y] not in '.0123456789'}

for x, row in enumerate(text):
    for y in re.finditer(r'\d+', row):
        edges = {(x, z) for x in (x - 1, x, x + 1) for z in range(y.start() - 1, y.end() + 1)}

        for edge in edges & board.keys():
            board[edge].append(int(y.group()))

print(sum(sum(number) for number in board.values()))
print(sum(math.prod(number) for number in board.values() if len(number) == 2))