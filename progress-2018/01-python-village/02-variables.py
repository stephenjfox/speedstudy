# The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths

from math import sqrt

def compute(a_side, b_side):
    # calculate hypotenuse
    hyp = sqrt(a_side ** 2 + b_side ** 2)

    # return the square of the hypotenuse
    return int(hyp ** 2)


with open('02-input.txt') as f:
    a, b = [int(x) for x in next(f).split(' ')]
    print(compute(a,b))
