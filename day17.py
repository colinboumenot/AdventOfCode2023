from heapq import heappop, heappush
text = open('inputTxt/day17input.txt').read().splitlines()
grid = {(x, y): int(heat) for x, line in enumerate(text) for y, heat in enumerate(line)}
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

heap = [(0, (0, 0), (0, 0))]
visited = {((0, 0), (0, 0))}
not_found = True

while not_found:
    heat, position, last_direction = heappop(heap)
    for direction in range(-1, 2):
        if direction == 0:
            if last_direction[1] == 3:
                continue
            else:
                dx = last_direction[1] + 1
        else:
            dx = 1

        new_direction = (last_direction[0] + direction) % 4
        new_position = ((position[0] + directions[new_direction][0]), (position[1] + directions[new_direction][1]))
        if (new_position in grid) and ((new_position, (new_direction, dx)) not in visited):
            new_heat = heat + grid[new_position]
            if new_position == (len(text) - 1, len(text[0]) - 1):
                print(new_heat)
                not_found = False
            visited.add((new_position, (new_direction, dx)))
            heappush(heap, (new_heat, new_position, (new_direction, dx)))

heap = [(0, (0, 0), (0, 0))]
visited = {((0, 0), (0, 0))}
not_found = True

while not_found:
    heat, position, last_direction = heappop(heap)
    for direction in range(-1, 2):
        if direction == 0:
            if last_direction[1] == 10:
                continue
            else:
                dx = last_direction[1] + 1
        else:
            if (0 < last_direction[1] < 4):
                continue
            dx = 1

        new_direction = (last_direction[0] + direction) % 4
        new_position = ((position[0] + directions[new_direction][0]), (position[1] + directions[new_direction][1]))
        if (new_position in grid) and ((new_position, (new_direction, dx)) not in visited):
            new_heat = heat + grid[new_position]
            if new_position == (len(text) - 1, len(text[0]) - 1):
                print(new_heat)
                not_found = False
            visited.add((new_position, (new_direction, dx)))
            heappush(heap, (new_heat, new_position, (new_direction, dx)))