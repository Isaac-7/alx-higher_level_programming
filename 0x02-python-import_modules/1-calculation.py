#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference multiple and quotient."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 10

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
