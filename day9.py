text = [[int(x) for x in line.split()] for line in open('inputTxt/day9input.txt').read().splitlines()]

def parse_line(line):
    if sum(x != 0 for x in line) == 0:
        return 0
    new_line = []
    for x in range(len(line) - 1):
        new_line.append(line[x + 1] - line[x])
    return line[-1] + parse_line(new_line)

answer = 0

for line in text:
    answer += parse_line(line)

print(answer)

answer = 0

for line in text:
    line = line[::-1]
    answer += parse_line(line)

print(answer)