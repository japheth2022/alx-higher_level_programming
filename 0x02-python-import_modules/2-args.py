#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    str1 = "argument"
    str2 = "arguments"
    num = (len(sys.argv) - 1)

    if num == 1:
        print("{} {}:".format(num, str1))
    elif num == 0:
        print("{} {}.".format(num, str2))
    else:
        print("{} {}:".format(num, str2))
    for index in range(1, num + 1):
        print("{}: {}".format(index, sys.argv[index]))
