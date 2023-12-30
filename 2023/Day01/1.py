import sys

d = open(sys.argv[1]).read().strip()

lines = d.split("\n")
digits = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}
key = list(digits.keys())


def treb(part2):
    ans = 0
    for line in lines:
        digit = ""
        if part2:
            for i in key:
                if i in line:
                    line = line.replace(i, digits[i])
        for c in line:
            if c.isnumeric():
                digit += c
        first = int(digit[0]) * 10
        second = int(digit[-1])
        ans += first + second
    return ans


print(treb(False))
print(treb(True))
