#!/usr/bin/python3
"""Read file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
