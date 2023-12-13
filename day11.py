from copy import deepcopy
text = open('inputTxt/day11input.txt').read().splitlines()

empty = []

for line in text:
    empty.append(line)
    if '#' not in line:
        empty.append(line)


text = list(zip(*empty))
empty = []

for line in text:
    empty.append(line)
    if '#' not in line:
        empty.append(line)

vertices = set()
text = deepcopy(empty)

for x in range(len(text)):
    for y in range(len(text[0])):
        if text[x][y] == '#':
            vertices.add((x, y))

vertices = list(vertices)
answer = 0

for x in range(len(vertices)):
    for y in range(x + 1, len(vertices)):
        answer += abs(vertices[x][0] - vertices[y][0]) + abs(vertices[x][1] - vertices[y][1])

print(answer)

text = open('inputTxt/day11input.txt').read().splitlines()

empty_rows = []

for x, line in enumerate(text):
    if '#' not in line:
        empty_rows.append(x)


empty_columns = []

temp_text = list(zip(*text))

for x, line in enumerate(temp_text):
    if '#' not in line:
        empty_columns.append(x)

vertices = set()
row_add = 0
column_add = 0

for x in range(len(text)):
    if x in empty_rows:
        row_add += 999999
    column_add = 0
    for y in range(len(text[0])):
        if y in empty_columns:
            column_add += 999999
        if text[x][y] == '#':
            vertices.add((x + row_add, y + column_add))

answer = 0

vertices = list(vertices)
for x in range(len(vertices)):
    for y in range(x + 1, len(vertices)):
        answer += abs(vertices[x][0] - vertices[y][0]) + abs(vertices[x][1] - vertices[y][1])

print(answer)

