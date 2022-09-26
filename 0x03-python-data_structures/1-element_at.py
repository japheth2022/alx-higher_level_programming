#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            print("none")
        if idx > i:
            print("none")
        else:
            print("{:d}".format(idx))
