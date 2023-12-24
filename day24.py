from itertools import combinations
import z3
text = open('inputTxt/day24input.txt').read().splitlines()

hailstones = list()

for line in text:
    positions, velocities = line.split('@')
    px, py, pz = positions.split(',')
    vx, vy, vz = velocities.split(',')
    slope = int(vy) / int(vx)
    intercept = int(py) - slope * int(px)
    hailstones.append([int(px), int(py), int(pz), int(vx), int(vy), int(vz), slope, intercept])

answer = 0

for line_one, line_two in combinations(hailstones, 2):
    if line_one[6] == line_two[6]:
        continue
    dx = (line_two[7] - line_one[7]) / (line_one[6] - line_two[6])
    dy = line_one[6] * dx + line_one[7]

    intersection_x = (line_two[7] - line_one[7]) / (line_one[6] - line_two[6])
    intersection_y = line_one[6] * intersection_x + line_one[7]

    time_one = (intersection_x - line_one[0]) / line_one[3]
    time_two = (intersection_x - line_two[0]) / line_two[3]

    if time_one < 0 or time_two < 0:
        continue

    if 200000000000000 <= intersection_x <= 400000000000000 and 200000000000000 <= intersection_y <= 400000000000000:
        answer += 1

print(answer)



solver = z3.Solver()
px, py, pz, vx, vy, vz = z3.Reals('px py pz vx vy vz')

for x, equation in enumerate(hailstones[0:3]):
    line = z3.Real(f"line{x}")
    solver.add(line > 0)
    solver.add(px + line * vx == equation[0] + line * equation[3])
    solver.add(py + line * vy == equation[1] + line * equation[4])
    solver.add(pz + line * vz == equation[2] + line * equation[5])
solver.check()
answer = sum(solver.model()[var].as_long() for var in [px, py, pz])
print(answer)