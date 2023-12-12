import sys

d = open(sys.argv[1]).read().strip()

lines = d.splitlines()

er = [x for x, row in enumerate(lines) if all(c == "." for c in row)]
ec = [x for x, col in enumerate(zip(*lines)) if all(c == "." for c in col)]
points = [
    (r, c) for r, row in enumerate(lines) for c, col in enumerate(row) if col == "#"
]


def f(xs):
    total = 0
    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[:i]:
            for x in range(min(x1, x2), max(x1, x2)):
                total += xs if x in er else 1
            for y in range(min(y1, y2), max(y1, y2)):
                total += xs if y in ec else 1
    return total


print("Part 1: " + str(f(2)))
print("Part 2: " + str(f(1000000)))
