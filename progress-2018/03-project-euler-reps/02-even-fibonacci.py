# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values
# __do not exceed four million__, find the sum of the even-valued terms.

def produce_fibs(under=100):
    a = b = 1
    while b < under:
        a, b = b, a + b
        if a % 2 == 0:
            yield a

from argparse import ArgumentParser

parser = ArgumentParser(description='Produce the sum of the even Fibonacci numbers')
parser.add_argument('up_to', type=int, nargs='?', default=4000000,
                    help='upper limit for which generate fibonacci numbers will not exceed')

ns = parser.parse_args()

print(sum(produce_fibs(ns.up_to)))
