import re
text = open('inputTxt/day1inputTxt.txt').read()

print(sum(int(line[0] + line[-1]) for line in re.sub(r"[A-z]", "", text).split("\n")))

stringNumbers = {
    'one' : 'o1e',
'two' : 't2o',
'three' : 'th3ee',
'four' : 'fo4r',
'five' : 'fi5e',
'six' : 's6x',
'seven' : 'se7en',
'eight' : 'ei8ht',
'nine' : 'n9ne',
}

for x, y in stringNumbers.items():
    text = text.replace(x, y)

print(sum(int(line[0] + line[-1]) for line in re.sub(r"[A-z]", "", text).split("\n")))