import itertools

text = open('inputTxt/day14input.txt').read().splitlines()

def move_rock(rock):
    for _ in range(100):
        rock = map(lambda x: x.replace('.O', 'O.'), rock)
    return rock

tilted_text = list(zip(*text))
for x, line in enumerate(tilted_text):
    tilted_text[x] = ''.join(line)

def sum_line(line):
    return sum(x * (item == 'O') for col in line for x, item in enumerate(col[::-1], 1))

print(sum_line(move_rock(tilted_text)))

text = open('inputTxt/day14input.txt').read().replace('\n', '')

def tilt(line, direction):
    if direction in 'nw':
        return ''.join(reversed(sorted(line)))
    else:
        return ''.join(sorted(line))

def sum_line(line):
    columns = [line[x::100] for x in range(100)]
    return sum(sum(x for x,y in zip(range(len(column), 0, -1), column) if y == 'O') for column in columns)
def rotate(text, direction):
    if direction in 'ns':
        columns = [text[x::100] for x in range(100)]
        for x, line in enumerate(columns):
            columns[x] = '#'.join(tilt(rock, direction) for rock in line.split('#'))
        return ''.join(itertools.chain(*zip(*columns)))
    if direction in 'ew':
        rows = [text[x * 100: (x + 1) * 100] for x in range(100)]
        for x, line in enumerate(rows):
            rows[x] = '#'.join(tilt(rock, direction) for rock in line.split('#'))
        return ''.join(rows)

current_cycle = 0
last_cycle = 1000000000

past_cycles = {}
repeat_cycle = False

while current_cycle < last_cycle:
    for direction in 'nwse':
        text = rotate(text, direction)

    current_cycle += 1

    if not repeat_cycle and (repeat_cycle := text in past_cycles):
        cycle_length = current_cycle - past_cycles[text]
        current_cycle += cycle_length * ((last_cycle - current_cycle) // cycle_length)
    else:
        past_cycles[text] = current_cycle

print(sum_line(text))