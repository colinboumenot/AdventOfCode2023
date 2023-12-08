import functools

text = open('inputTxt/day7input.txt').read().splitlines()

values = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}

fives, fours, full_house, threes, twos, pairs, highs = [], [], [], [], [], [], []

for line in text:
    hand = line.split()[0]

    if len(set(list(hand))) == 1:
        fives.append(line)
    elif len(set(list(hand))) == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            fours.append(line)
        else:
            full_house.append(line)
    elif len(set(list(hand))) == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            threes.append(line)
        else:
            twos.append(line)
    elif len(set(list(hand))) == 4:
        pairs.append(line)
    else:
        highs.append(line)


def compare(hand_one, hand_two):
    for x in range(6):
        if values[hand_one[x]] > values[hand_two[x]]:
            return -1
        if values[hand_one[x]] < values[hand_two[x]]:
            return 1
    return 0

fives = sorted(fives, key = functools.cmp_to_key(compare))
fours = sorted(fours, key = functools.cmp_to_key(compare))
full_house = sorted(full_house, key = functools.cmp_to_key(compare))
threes = sorted(threes, key = functools.cmp_to_key(compare))
twos = sorted(twos, key = functools.cmp_to_key(compare))
pairs = sorted(pairs, key = functools.cmp_to_key(compare))
highs = sorted(highs, key = functools.cmp_to_key(compare))

ranks = fives + fours + full_house + threes + twos + pairs + highs

counter = 1
answer = 0
for line in reversed(ranks):
    answer += counter * int(line.split()[1])
    counter += 1

print(answer)

values = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'T' : 10, 'J' : 0, 'Q' : 12, 'K' : 13, 'A' : 14}

fives, fours, full_house, threes, twos, pairs, highs = [], [], [], [], [], [], []

for line in text:
    hand = line.split()[0]

    if len(set(list(hand))) == 1:
        fives.append(line)
    elif len(set(list(hand))) == 2:
        if 'J' in hand:
            fives.append(line)
        elif hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            fours.append(line)
        else:
            full_house.append(line)
    elif len(set(list(hand))) == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            if 'J' in hand:
                fours.append(line)
            else:
                threes.append(line)
        else:
            if 'J' in hand:
                if hand.count('J') == 2:
                    fours.append(line)
                else:
                    full_house.append(line)
            else:
                twos.append(line)
    elif len(set(list(hand))) == 4:
        if 'J' in hand:
            threes.append(line)
        else:
            pairs.append(line)
    else:
        if 'J' in hand:
            pairs.append(line)
        else:
            highs.append(line)

fives = sorted(fives, key = functools.cmp_to_key(compare))
fours = sorted(fours, key = functools.cmp_to_key(compare))
full_house = sorted(full_house, key = functools.cmp_to_key(compare))
threes = sorted(threes, key = functools.cmp_to_key(compare))
twos = sorted(twos, key = functools.cmp_to_key(compare))
pairs = sorted(pairs, key = functools.cmp_to_key(compare))
highs = sorted(highs, key = functools.cmp_to_key(compare))

ranks = fives + fours + full_house + threes + twos + pairs + highs

counter = 1
answer = 0
for line in reversed(ranks):
    answer += counter * int(line.split()[1])
    counter += 1

print(answer)