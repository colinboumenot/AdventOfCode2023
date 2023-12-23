from collections import deque
from copy import deepcopy

text = open('inputTxt/day23input.txt').read().splitlines()

grid = {}
for x, line in enumerate(text):
    for y, character in enumerate(line):
        grid[x, y] = character


directions = {'v': (1, 0), '^': (-1, 0), '>': (0, 1), '<': (0, -1)}

def neighbors(x, y):
    if grid[x, y] in ['v', '^', '>', '<']:
        yield x + directions[grid[x, y]][0], y + directions[grid[x, y]][1]
        return

    for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        dx = x + direction[0]
        dy = y + direction[1]
        if (dx, dy) not in grid or grid[dx, dy] == '#':
            continue
        yield dx, dy

def bfs(start, end):
    nodes = deque([(*start, set())])
    cost = dict()
    cost[start] = 0

    while nodes:
        x, y, path = nodes.pop()

        if (x, y) == end:
            continue

        for neighbor in neighbors(x, y):
            new_cost = cost[x, y] + 1

            if neighbor in path:
                continue

            if neighbor not in cost or new_cost > cost[neighbor]:
                cost[neighbor] = new_cost
                new_path = path.copy()
                new_path.add(neighbor)
                nodes.appendleft((*neighbor, new_path))

    return cost[end]


start = (0, 1)
end = (140, 139)
print(bfs(start, end))

grid = tuple(text)

def new_neighbors(x, y):
    for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        dx = x + direction[0]
        dy = y + direction[1]
        if 0 <= dx < len(grid[0]) and 0 <= dy < len(grid):
            if grid[dy][dx] != '#':
                yield (dx, dy)

def count_length(edges, start, end):
    count = 1
    while len(edges[end]) == 2:
        count += 1
        next = [n for _, n in edges[end] if n != start][0]
        start, end = (end, next)
    return (count, end)

def crossings():
    edges = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != '#':
                edges[(y, x)] = [(1, n) for n in new_neighbors(y, x)]
    newedges = {}
    for x, y in edges.items():
        if len(y) != 2:
            newedges[x] = [count_length(edges, x, n[1]) for n in y]
    return newedges

def dfs(crossings, start, end):
    visited = set([start])
    stack = [(start, 0, visited)]
    max_length = 0

    while stack:
        current, path, visited = stack.pop()
        if current == end:
            max_length = max(max_length, path)
        for x, neighbor in crossings[current]:
            if neighbor not in visited:
                stack.append((neighbor, path + x, visited | set([neighbor])))
    return max_length



print(dfs(crossings(), (1, 0), (len(grid[0]) - 2, len(grid) - 1)))