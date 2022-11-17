#!/usr/bin/python3

"""Defines a functions that reads a UTF8 text file"""


def read_file(filename=""):

    """Print a UTF* textfile inthe stdout"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
