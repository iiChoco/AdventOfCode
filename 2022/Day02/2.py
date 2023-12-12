import sys

d = open(sys.argv[1]).read().strip()
lines = d.split("\n")


def part1():
    score = 0
    for line in lines:
        if line[0] == "A" and line[-1] == "X":
            score += 3
        if line[0] == "B" and line[-1] == "Y":
            score += 3
        if line[0] == "C" and line[-1] == "Z":
            score += 3
        if line[0] == "A" and line[-1] == "Y":
            score += 6
        if line[0] == "B" and line[-1] == "Z":
            score += 6
        if line[0] == "C" and line[-1] == "X":
            score += 6
        if line[-1] == "X":
            score += 1
        if line[-1] == "Y":
            score += 2
        if line[-1] == "Z":
            score += 3
    return score


def part2():
    count = 0
    score = 0
    for line in lines:
        winMap = {"A": "Y", "B": "Z", "C": "X"}
        tieMap = {"A": "X", "B": "Y", "C": "Z"}
        loseMap = {"A": "Z", "B": "X", "C": "Y"}

        opponent, me = line.split()
        if me == "X":
            me = loseMap[opponent]
        if me == "Y":
            me = tieMap[opponent]
            score += 3
        if me == "Z":
            me = winMap[opponent]
            score += 6

        if me == "X":
            score += 1
        if me == "Y":
            score += 2
        if me == "Z":
            score += 3
        count += 1
    print(count)
    return score


print(part2())
