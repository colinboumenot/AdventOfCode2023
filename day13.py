text = open('inputTxt/day13input.txt').read().split('\n\n')

def find_symmetry(lines, skip = None):

    for x in range(len(lines) - 1):
        line = (x, None)
        if line == skip:
            continue

        left = lines[:x + 1][::-1]
        right = lines[x + 1:]

        mirror = True

        for y in range(min(len(left), len(right))):
            if left[y] != right[y]:
                mirror = False
                break

        if mirror:
            return (line, 100 * len(left))

    for y in range(len(lines[0]) - 1):
        line = (None, y)
        if line == skip:
            continue

        left = [lines[x][:y + 1][::-1] for x in range(len(lines))]
        right = [lines[x][y + 1:] for x in range(len(lines))]

        mirror = True

        for x in range(min(len(left[0]), len(right[0]))):
            if [item[x] for item in left] != [item[x] for item in right]:
                mirror = False
                break

        if mirror:
            return (line, len(left[0]))

answer = 0

for line in text:
    line = [[x for x in row] for row in line.split('\n')]
    answer += find_symmetry(line)[1]

print(answer)

def find_smudge(lines):
    line = find_symmetry(lines)[0]

    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == '.':
                lines[x][y] = '#'
            else:
                lines[x][y] = '.'
            new_line = find_symmetry(lines, line)
            if new_line != None and new_line[0] != line:
                return new_line[1]
            if lines[x][y] == '.':
                lines[x][y] = '#'
            else:
                lines[x][y] = '.'

answer = 0

for line in text:
    line = [[x for x in row] for row in line.split('\n')]
    answer += find_smudge(line)

print(answer)
