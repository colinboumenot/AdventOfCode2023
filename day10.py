text = open('inputTxt/day10input.txt').read().splitlines()


north = (-1, 0)
east = (0, 1)
south = (1, 0)
west = (0, -1)

pipes = {
    'S': [north, south, west, east],
    '|': [north, south],
    'L': [north, east],
    'J': [north, west],
    '7': [south, west],
    'F': [south, east],
    '-': [west, east],
    '.': []
}

start = None

for x in range(len(text)):
    for y in range(len(text[0])):
        if text[x][y] == 'S':
            start = (x, y)

def travel(map, pipe, direction):
    distance = 0
    x, y = pipe
    visited_pipes = set()

    while (x, y) != pipe or distance == 0:
        visited_pipes.add((x, y))
        dx, dy = direction
        x += dx
        y += dy

        if not (0 <= x < len(map)) and (0 <= y < len(map[0])):
            return None

        dx *= -1
        dy *= -1
        move_directions = pipes[text[x][y]]

        if (dx, dy) not in move_directions:
            return None

        for move in move_directions:
            if move != (dx, dy):
                direction = move
        distance += 1
    return distance, visited_pipes

result = None
loops = []

for move in north, east, south, west:
    loop = travel(text, start, move)
    if loop is not None:
        result = loop
        loops.append(move)
print(result[0] // 2)

hand = None
answer = 0
pipes["S"] = loops

for x in range(len(text)):
    inner = False
    for y in range(len(text[0])):
        if (x, y) in result[1]:
            direction = pipes[text[x][y]]
            if east in direction and west in direction:
                continue
            inner = not inner
            if north in direction and south in direction:
                continue
            temp = None
            for dir in direction:
                if dir != east and dir != west:
                    temp = dir
            if hand == None:
                hand = temp
            else:
                if temp != hand:
                    inner = not inner
                hand = None
        else:
            if inner:
                answer += 1
print(answer)









