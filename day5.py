import re
from functools import reduce

text = open('inputTxt/day5input.txt').read().splitlines()
seeds = [int(x) for x in text[0].split(':')[1].split()]

def parse(text):
    x = 3
    while x < len(text):
        current = []
        while x < len(text) and text[x] != '':
            two, one, length = (int(x) for x in text[x].split())
            current.append([one, one + length, two - one])
            x += 1
        yield sorted(current)
        x += 2

maps = list(parse(text))

def translate(map, pair):
    for start, end in pair:
        for x, y, z in map:
            yield(start, min(x, end))
            yield (max(x, start) + z, min(y, end) + z)
            start = max(start, min(y, end))
        yield (start, end)

def solve(map, seed):
    for m in map:
        seed = [(x, y) for x, y in translate(m, seed) if x < y]
    return min(x for x, y in seed)

print(solve(maps, ((x, x + 1) for x in seeds)))
print(solve(maps, ((x, x + y) for x, y in zip(seeds[::2], seeds[1::2]))))