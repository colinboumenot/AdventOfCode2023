text = open('inputTxt/day21input.txt').read().splitlines()
grid = []

for x, line in enumerate(text):
    grid.append(list())
    for y, character in enumerate(line):
        if character == 'S':
            start = (y, x)
            grid[x].append('.')
        else:
            grid[x].append(character)


plots = set()
plots.add(start)

for x in range(64):
    new_plots = set()
    for plot in plots:
        x = plot[0]
        y = plot[1]
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if grid[y + direction[1]][x + direction[0]] == '.':
                new_plots.add((x + direction[0], y + direction[1]))
        plots = new_plots

print(len(plots))

from collections import deque

def solve(step):
    grid = []
    for _ in range(5):
        for line in text:
            grid.append(5 * line.replace('S', '.'))

    plots = deque()
    plots.append((len(grid[0]) // 2, len(grid) // 2, 0))
    total = set()
    visited = set()

    while plots:
        x, y, steps = plots.popleft()
        if (x, y, steps) in visited:
            continue
        visited.add((x, y, steps))
        if steps == step:
            total.add((x, y))
        else:
            if x >= 0:
                if grid[y][x - 1] != '#':
                    plots.append((x - 1, y, steps + 1))
                if x < len(grid[0]) - 1:
                    if grid[y][x + 1] != '#':
                        plots.append((x + 1, y, steps + 1))
                if y >= 0:
                    if grid[y - 1][x] != '#':
                        plots.append((x, y - 1, steps + 1))
                if y < len(grid) - 1:
                    if grid[y + 1][x] != '#':
                        plots.append((x, y + 1, steps + 1))
    return len(total)

a = solve(65)
b = solve(65 + 131)
c = solve(65 + 2 * 131)

import numpy as np

x = np.matrix([[0, 0, 1], [1, 1, 1], [4, 2, 1]])
y = np.array([a, b, c])
equation = np.linalg.solve(x, y).astype(np.int64)

print(equation[0] * 202300 * 202300 + equation[1] * 202300 + equation[2])

