text = open('inputTxt/day22input.txt').read().splitlines()

grid = [[[int(num) for num in position.split(',')] for position in brick.split('~')] for brick in text]
grid.sort(key = lambda x: x[0][2])
bricks = [{(x, y, z) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) for z in range(z1, z2 + 1)} for (x1, y1, z1), (x2, y2, z2) in grid]

falling = {}
graph = {x: set() for x in range(len(bricks))}

for x, brick in enumerate(bricks):
    next_brick = {(x, y, z - 1) for x, y, z in brick}
    intersection = {falling.get(position) for position in next_brick if position in falling}
    while not intersection and not any(pos[-1] == 0 for pos in brick):
        brick = next_brick
        next_brick = {(x, y, z - 1) for x, y, z in brick}
        intersection = {falling.get(position) for position in next_brick if position in falling}
    falling |= {position: x for position in brick}
    for b in intersection:
        graph[b].add(x)

from collections import defaultdict

supported = defaultdict(set)
for key, value in graph.items():
    for v in value:
        supported[v].add(key)

removable = set()

for key, value in graph.items():
    if not value or all(len(supported[x]) > 1 for x in value):
        removable.add(key)
print(len(removable))

def bricks_destroyed(brick):
    destroyed = 0
    visited = set()
    from collections import deque
    queue = deque([brick])
    while queue:
        current = queue.popleft()
        visited.add(current)
        for x in graph[current]:
            if len(supported[x] - visited) == 0:
                destroyed += 1
                queue.append(x)
    return destroyed

print(sum(bricks_destroyed(brick) for brick in (set(range(len(bricks))) - removable)))
