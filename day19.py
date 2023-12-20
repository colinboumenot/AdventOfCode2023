from copy import deepcopy

text = open('inputTxt/day19input.txt').read().split('\n\n')

instructions = {}
for line in text[0].split('\n'):
    line = line.split('{')
    name = line[0]
    parts = [part.split(':') for part in line[1][:-1].split(',')]
    parts = [[(part[0][0], part[0][1], int(part[0][2:])), part[1]] if len(part) == 2 else part for part in parts]
    instructions[name] = parts
ratings = []
for line in text[1].split('\n'):
    line = [x.split('=') for x in line[1:-1].split(',')]
    line = dict((key, int(value)) for [key, value] in line)
    ratings.append(line)

answer = 0

for rating in ratings:
    current = 'in'
    while current not in ['A', 'R']:
        rules = instructions[current]
        for rule in rules:
            if len(rule) == 1:
                current = rule[0]
                break
            else:
                (category, decision, value) = rule[0]
                end_spot = rule[1]

                if decision == '>':
                    if rating[category] > value:
                        current = end_spot
                        break
                elif decision == '<':
                    if rating[category] < value:
                        current = end_spot
                        break
    if current == 'A':
        answer += sum(rating.values())
print(answer)

def find_range(range):
    value = 1
    for x in range.values():
        value *= 1 + x[1] - x[0]
    return value

def range_solve(instructions, ranges, current):
    parts = instructions[current]
    value = 0

    for part in parts:
        if len(part) == 1:
            if part[0] == 'A':
                value += find_range(ranges)
            elif part[0] != 'R':
                value += range_solve(instructions, ranges, part[0])
        else:
            (variable, condition, total) = part[0]
            end_spot = part[1]
            new_range = ranges[variable]

            if condition == '>':
                if new_range[1] > total:
                    temp_range = deepcopy(ranges)
                    temp_range[variable] = (max(new_range[0], total + 1), new_range[1])

                    if end_spot == 'A':
                        value += find_range(temp_range)
                    elif end_spot != 'R':
                        value += range_solve(instructions, temp_range, end_spot)

                ranges[variable] = (new_range[0], total)
            else:
                if new_range[0] < total:
                    temp_range = deepcopy(ranges)
                    temp_range[variable] = (new_range[0], min(new_range[1], total - 1))

                    if end_spot == 'A':
                        value += find_range(temp_range)
                    elif end_spot != 'R':
                        value += range_solve(instructions, temp_range, end_spot)
                ranges[variable] = (total, new_range[1])
    return value

ranges = {}

for value in 'xmas':
    ranges[value] = (1, 4000)
answer = range_solve(instructions, ranges, 'in')

print(answer)


