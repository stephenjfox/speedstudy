from collections import Counter

# Given: a string of no more than 10000 letters
# Return: Word count, in any order, i.e any 1 <line break> word 2

c = Counter()

with open('06-input.txt') as input:
    text = input.readline()

    for value in text.split(' '):
        c[value] += 1

for word, count in c.items():
    print(word, count)
