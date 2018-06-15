# START: Prompt
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23. (3 + 5 + 6 + 9 = 23)

# Find the sum of all the multiples of 3 or 5 below 1000.
# END: Prompt


# Fizzbuzz is a program that does special printing for multiples of 3, 5, and 15
# This program is just to sum those numbers, rather than printing them


def generate_multiples(up_to=1000):
    for n in range(up_to):
        if n % 3 == 0 or n % 5 == 0:
            yield n

print(sum(generate_multiples(1000)))
