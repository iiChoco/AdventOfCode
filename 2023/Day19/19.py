import sys

D = open(sys.argv[1]).read().strip()

instruction, given = D.split("\n\n")

rules = instruction.split("\n")


def parseRules(xs):
    xs = xs[2:-3]
    print(xs)
    rules = xs.split(",")
    print(rules)


print(instruction)
parseRules(rules)
for line in rules:
    parseRules(line)
