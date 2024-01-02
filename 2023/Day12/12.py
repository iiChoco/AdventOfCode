import sys

d = open(sys.argv[1]).read().strip()

L = d.split("\n")

total = 0


def springs(spring, group):
    if not spring:
        return 1 if not group else 0
    elif spring[0] == ".":
        return springs(spring[1:], group)
    elif spring[0] == "?":
        return int(springs("#" + spring[1:], group)) + int(
            springs("." + spring[1:], group)
        )
    elif spring[0] == "#" and group:
        if len(spring) >= int(group[0]) and all(
            spring[x] != "." for x in range(int(group[0]))
        ):
            spring = spring[int(group[0]) :]
            group.pop(0)
            return springs(spring, group)
    return 0


for line in L:
    spring, group = line.split()
    group = group.split(",")
    temp = int(springs(spring, group))
    total += temp
print(total)
