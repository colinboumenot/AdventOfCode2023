from collections import deque
from math import lcm

text = open('inputTxt/day20input.txt').read().splitlines()

modules = {}
standards = {}
conjunctions = {}

for line in text:
    module, connections = line.split(' -> ')
    connections = connections.split(', ')

    if module == 'broadcaster':
        marker = None
        modules['broadcaster'] = connections
    else:
        marker = module[0]
        module = module[1:]
        modules[module] = connections

    if marker == '&':
        conjunctions[module] = {}

    if marker == '%':
        standards[module] = False

for module, destination in modules.items():
    for x in destination:
        if x in conjunctions:
            conjunctions[x][module] = 0

rx_presses = {}

def pulse(presses):
    high = 0
    low = 1 + len(modules['broadcaster'])
    queue = deque()

    for module in modules['broadcaster']:
        queue.append((0, 'broadcaster', module))

    while queue:
        state, source, module = queue.popleft()

        if module == 'rx':
            continue

        sent = 0
        if module in standards:
            if state == 1:
                continue
            standards[module] = not standards[module]
            if standards[module]:
                sent = 1
        if module in conjunctions:
            conjunctions[module][source] = state
            if any(x == 0 for x in conjunctions[module].values()):
                sent = 1

        if sent == 1:
            high += len(modules[module])
        else:
            low += len(modules[module])

        for destination in modules[module]:
            queue.append((sent, module, destination))

        for item, value in conjunctions['zh'].items():
            if value == 1 and item not in rx_presses:
                rx_presses[item] = presses

    return high, low

high = 0
low = 0
presses = 0

for _ in range(1000):
    presses += 1
    new_high, new_low = pulse(presses)
    high += new_high
    low += new_low

print(high * low)

while len(rx_presses) < 4:
    presses += 1
    pulse(presses)

print(lcm(*rx_presses.values()))


