import math
import re

text = open('inputTxt/day8input.txt').read().splitlines()

moves = {}

for x, line in enumerate(text):
    line = line.strip()

    if x == 0:
        directions = line
    elif x > 1:
        current, left, right = re.findall('\w+', line)
        moves[current] = (left, right)

answer = 0
direction_counter = -1
location = 'AAA'

while location != 'ZZZ':
    answer += 1
    direction_counter += 1

    if direction_counter == len(directions):
        direction_counter = 0

    direction = directions[direction_counter]

    if direction == 'L':
        location = moves[location][0]
    else:
        location = moves[location][1]

print(answer)

def solve(start):
    current = start
    steps = 0
    while not current.endswith('Z'):
        direction = directions[steps % len(directions)]

        if direction == 'L':
            current = moves[current][0]
        else:
            current = moves[current][1]
        steps += 1
    return steps

answer = 1

for move in moves:
    if move.endswith('A'):
        answer = math.lcm(answer, solve(move))

print(answer)
