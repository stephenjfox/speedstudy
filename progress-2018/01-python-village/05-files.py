# Given: A file containing at most 1000 lines of text
# Return: A file containing all of the even-numbered lines, assuming 1-based line numberings

with open('05-input.txt') as input_text, open('05-output.txt', 'w+') as output:
    for i, line in enumerate(input_text):
        if i % 2 == 1: # if we're on a 0-based "odd line", 1-based "even line"
            print(line.strip(), file=output)
