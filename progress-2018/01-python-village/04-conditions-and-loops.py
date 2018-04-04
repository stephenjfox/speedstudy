# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

with open('04-input.txt') as f:
    bottom, top = [int(x) for x in f.readline().split(' ')]
    bottom += 1 if bottom % 2 == 0 else 0 # for an odd start
    print(sum(n for n in range(bottom, top, 2)))
