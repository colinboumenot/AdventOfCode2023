text = list(map(str.split, open('inputTxt/day18input.txt')))

directions = {'R' : (1, 0), 'D' : (0, 1), 'L' : (-1, 0), 'U' : (0, -1)}

lines = [(directions[direction], int(moves)) for direction, moves, _ in text]
position = 0
answer = 1
for (x, y), z in lines:
    position += x * z
    answer += y * z * position + z / 2

print(int(answer))

directions = {'0' : (1, 0), '1' : (0, 1), '2' : (-1, 0), '3' : (0, -1)}

lines = [(directions[hex[7]], int(hex[2:7], 16)) for _, _, hex in text]
position = 0
answer = 1
for (x, y), z in lines:
    position += x * z
    answer += y * z * position + z / 2

print(int(answer))