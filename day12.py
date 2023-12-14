text = [line.split() for line in open('inputTxt/day12input.txt').read().splitlines()]

def combinations(line, springs, answer = 0):
    if not springs:
        return '#' not in line

    current, springs = springs[0], springs[1:]

    for x in range(len(line) - sum(springs) - len(springs) - current + 1):
        if '#' in line[:x]:
            break
        if (nxt := x + current) <= len(line) and '.' not in line[x : nxt] and line[nxt : nxt + 1] != '#':
            answer += combinations(line[nxt + 1:], springs)
    return answer

answer_one = 0
answer_two = 0

for x, (line, springs) in enumerate(text):
    answer_one += combinations(line, (springs := tuple(map(int, springs.split(',')))))
    answer_two += combinations('?'.join([line] * 5), springs * 5)

print(answer_one)
print(answer_two)