#!/usr/bin/python3
for chars in range(97, 123):
    if chars in [101, 113]:
        continue
    print("{:c}".format(chars), end='')

