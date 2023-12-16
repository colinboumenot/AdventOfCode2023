text = open('inputTxt/day15input.txt').read()
#text = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

def sum_line(line):
    sum = 0
    for character in line:
        sum += ord(character)
        sum = (17 * sum) % 256
    return sum

text = text.split(',')

answer = 0

for line in text:
    answer += sum_line(line)

print(answer)

from collections import defaultdict

boxes = defaultdict(dict)

for line in text:
    if '=' in line:
        label, number = line.split('=')
        boxes[sum_line(label)][label] = int(number)
    elif '-' in line:
        label = line[:-1]
        boxes[sum_line(label)].pop(label, None)

answer = 0

for box in boxes:
    for x, value in enumerate(boxes[box].values()):
        answer += (box + 1) * (x + 1) * value

print(answer)