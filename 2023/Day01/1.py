d = open("orange.in").read().strip()
lines = d.split('\n')
p1 = 0
p2 = 0
digits = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
        }
key = list(digits.keys())
for line in lines:
    digit = ""
    for i in key:
        if i in line:
            line = line.replace(i, digits[i])
    for c in line:
        if c.isnumeric():

            digit += c
    first = int(digit[0]) * 10
    second = int(digit[-1])
    p1 += first + second
print(p1)
