#!/usr/bin/python3
"""Factorize as many numbers as possible"""


from sys import argv
def factorize(value):
    x = 2

    if value < 2:
        return
    print()
    print(value, "<- value-bef")
    while value % x:
        x += 1
    print("{:.0f}={:.0f}*{:.0f}".format(value, value/x, x))
    print(value, "< value-aft")
    print()

if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            value = int(line.split('\n')[0])
            factorize(value)
            line = file.readline()
except:
    pass
