import sys

d = open(sys.argv[1]).read().strip()

L = d.split("\n")


def f(spring, group):
    if spring[0] == ".":
        spring = spring[1]
        return f(spring, group)
    if spring[0] == "?":
        spring = str(0) + spring[1:]
        return f(spring, group)
    if spring[0] == "#":
        if all(spring[i] == "#" for i in range(int(group[0]))):
            spring = spring[: range(int(group[0]))]
            group.pop(0)
            return f(spring, group)
    if spring == "" and not group:
        return 1
    elif spring == "" and group:
        return 0
    return 0


count = 0
for line in L:
    a, b = line.split()
    print(a, b)
    b = b.split(",")
    count += int(f(a, b))
print(count)
