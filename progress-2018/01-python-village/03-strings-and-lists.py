with open('03-input.txt') as f:
    text = f.readline()
    start, start_bound, end, end_bound = [int(x) for x in f.readline().split(' ')]

    print(text[start:start_bound + 1], text[end: end_bound + 1])
