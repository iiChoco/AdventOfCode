import sys

d = open(sys.argv[1]).read().strip()

lines = d.split("\n")


def cube(part2):
    ans = 0
    for line in lines:
        ok = True
        mR, mG, mB = (12, 13, 14) if not part2 else (0, 0, 0)
        ID, info = line.split(":")
        rounds = info.split(";")
        r, g, b = "0", "0", "0"
        for round in rounds:
            split = round.split(",")
            for x in split:
                if "red" in x:
                    r = x
                if "green" in x:
                    g = x
                if "blue" in x:
                    b = x
            r = "".join(filter(lambda x: x.isdigit(), r))
            if not part2:
                if int(r) > mR:
                    ok = False
            else:
                if int(r) > mR:
                    mR = int(r)
            g = "".join(filter(lambda x: x.isdigit(), g))
            if not part2:
                if int(g) > mG:
                    ok = False
            else:
                if int(g) > mG:
                    mG = int(g)
            b = "".join(filter(lambda x: x.isdigit(), b))
            if not part2:
                if int(b) > mB:
                    ok = False
            else:
                if int(b) > mB:
                    mB = int(b)

        if ok and not part2:
            ID = "".join(filter(lambda x: x.isdigit(), ID))
            ans += int(ID)
        elif part2:
            ans += mR * mG * mB
    return ans


print(cube(False))
print(cube(True))
