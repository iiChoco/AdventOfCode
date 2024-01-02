import sys

d = open(sys.argv[1]).read().strip()
lines = d.split("\n")
p1 = 0
p2 = 0


def difference1(x):
    p = []
    for i in range(len(x) - 1):
        p.append(x[i + 1] - x[i])
    if all(h == 0 for h in p):
        return x[-1]
    else:
        return x[-1] + difference1(p)


def difference2(x):
    p = []
    for i in range(len(x) - 1):
        p.append(x[i + 1] - x[i])
    if all(h == 0 for h in p):
        return x[0]
    else:
        return x[0] - difference2(p)


for line in lines:
    xs = [int(x) for x in line.split()]
    p1 += difference1(xs)
    p2 += difference2(xs)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
