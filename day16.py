text = open('inputTxt/day16input.txt').read().splitlines()

directions = {'Right' : (0, 1), 'Left' : (0, -1), 'Up' : (-1, 0), 'Down' : (1, 0)}

def move_beams(start):
    queue = [start]
    visited = set()
    energized = set()

    while queue:
        current = queue.pop()

        if current in visited:
            continue

        visited.add(current)
        energized.add(current[0])
        direction = current[1]
        new = (current[0][0] + directions[direction][0], current[0][1] + directions[direction][1])

        if not (0 <= new[0] < len(text)) or not (0 <= new[1] < len(text[new[0]])):
            continue

        mirror = text[new[0]][new[1]]

        if mirror == '\\':
            if direction == 'Right':
                direction = 'Down'
            elif direction == 'Up':
                direction = 'Left'
            elif direction == 'Left':
                direction = 'Up'
            elif direction == 'Down':
                direction = 'Right'
            queue.append((new, direction))
        elif mirror == '/':
            if direction == 'Right':
                direction = 'Up'
            elif direction == 'Up':
                direction = 'Right'
            elif direction == 'Left':
                direction = 'Down'
            elif direction == 'Down':
                direction = 'Left'
            queue.append((new, direction))
        elif mirror == '|' and direction in ['Right', 'Left']:
            queue.append((new, 'Up'))
            queue.append((new, 'Down'))
        elif mirror == '-' and direction in ['Up', 'Down']:
            queue.append((new, 'Right'))
            queue.append((new, 'Left'))
        else:
            queue.append((new, direction))

    return len(energized) - 1


print(move_beams(((0, -1), 'Right')))

max_answer = 0

for x in range(len(text)):
    max_answer = max(max_answer, move_beams(((x, -1), 'Right')))
    max_answer = max(max_answer, move_beams(((x, len(text[0])), 'Left')))
for x in range(len(text[0])):
    max_answer = max(max_answer, move_beams(((-1, x), 'Down')))
    max_answer = max(max_answer, move_beams(((len(text), x), 'Up')))

print(max_answer)


