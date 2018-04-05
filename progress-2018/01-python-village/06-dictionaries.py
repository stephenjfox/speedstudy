from collections import Counter

with open('./06-input.txt') as source, open('./06-output.txt', mode='w+') as out:
    counter = Counter()
    for line in source:
        for word in line.split():
            counter[word] += 1

    for key, value in counter.items():
        print(key, value, file=out)
