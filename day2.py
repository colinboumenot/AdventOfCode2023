text = open('inputTxt/day2input.txt').read()

text = [line.split(':')[1] for line in text.splitlines()]

def check_lines(line):
    lines = [game.strip() for game in line.split(';')]
    for line in lines:
        if not valid_line(line):
            return False
    return True

def valid_line(line):
    moves = line.split(',')
    for move in moves:
        move = move.split()
        value = int(move[0])
        color = move[1]

        if not ((color == 'red' and value <= 12) or (color == 'green' and value <= 13) or (color == 'blue' and value <= 14)):
            return False

    return True

answer = 0

for id, line in enumerate(text):
    id += 1
    if check_lines(line):
        answer += id

print(answer)

text = open('inputTxt/day2input.txt').read()

text = [line.split(':')[1] for line in text.splitlines()]

def valid_line_two(line):
    line = line.replace(';', ',')
    max_red = 0
    max_green = 0
    max_blue = 0

    moves = line.split(',')
    for move in moves:
        move = move.split()
        value = int(move[0])
        color = move[1]

        if color == 'red' and value > max_red:
            max_red = value
        if color == 'green' and value > max_green:
            max_green = value
        if color == 'blue' and value > max_blue:
            max_blue = value

    return max_red * max_green * max_blue

answer = 0

for line in text:
    answer += valid_line_two(line)

print(answer)