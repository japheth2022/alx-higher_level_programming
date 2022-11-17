#!/usr/bin/python3
"""Defines a function that writes a  string to a UTF8 file"""


def write_file(filename="", text=""):

    """writes a string and returns the characters"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
