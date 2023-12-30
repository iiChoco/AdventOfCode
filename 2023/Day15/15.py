import sys

D = open(sys.argv[1]).read().strip()

hash = D.split(",")


def f():
    total = 0
    for h in hash:
        current = 0
        for c in h:
            current += ord(c)
            current *= 17
            current = current % 256
        total += current
    return total


print(f())
