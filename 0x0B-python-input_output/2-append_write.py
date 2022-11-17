#!/usr/bin/python3

"""Defines a method that appends a string at the end of  file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file.
    Returns the characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.append(text)
