#!/usr/bin/env python3
from unicodedata import digit


def print_last_digit(number):
    if number < 0:
        last_digit = number % -10
    else:
        last_digit = number % 10
    print("{}".format(last_digit), end="")
    return (last_digit)
