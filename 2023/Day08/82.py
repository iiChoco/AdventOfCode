import sys

d = open(sys.argv[1]).read().strip()
lines = d.split("\n")

bobs = []
steps = []
dict = {}
count = 0

for char in lines[0]:
    steps.append(char)
steps *= 100000000000  # Repeated steps
lines.pop(0)
lines.pop(0)

for line in lines:
    if line[2] == "A":
        bobs.append(line[:3])

for i, line in enumerate(lines):
    dict[line[:3]] = line[6:]

for bob in bobs:
    while bob[-1] != "Z":
        key = bob
        left = dict[key][1:4]
        right = dict[key][6:9]

        if steps[count] == "L":
            bob = left
            count += 1
        elif steps[count] == "R":
            bob = right
            count += 1

print(count)

