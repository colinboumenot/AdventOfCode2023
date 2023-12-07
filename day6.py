text = open('inputTxt/day6input.txt').read().splitlines()

times = [int(x) for x in text[0].split(':')[1].split()]
records = [int(x) for x in text[1].split(':')[1].split()]
print(times)
print(records)

def distance(time, records):
    wins = 0
    for x in range(time + 1):
        distance = x * (time - x)
        if distance > records:
            wins += 1
    return wins

answer = 1
for x in range(len(times)):
    answer *= distance(times[x], records[x])
print(answer)
print(int(distance(41777096, 249136211271011)))



