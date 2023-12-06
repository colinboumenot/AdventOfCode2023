text = open('inputTxt/day4input.txt').read().splitlines()

def score(winning, user):
    x = len(set(winning) & set(user))
    if x > 0:
        return 2 ** (x - 1)
    else:
        return 0


answer = 0
cards = [1 for line in text]

for index, line in enumerate(text):
    line = line.split(':')[1]
    winning, user = line.split('|')
    winning = winning.split()
    user = user.split()
    answer += score(winning, user)
    y = score(winning, user)

    for x in range(len(set(winning) & set(user))):
        cards[index + x + 1] += cards[index]

print(answer)
print(sum(cards))


