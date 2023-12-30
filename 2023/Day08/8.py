import sys
import math
import time

d = open(sys.argv[1]).read().strip()
lines = d.split("\n")

start_time = time.time()
bobs = []
steps = []
dict = {}
lol = []
for char in lines[0]:
    steps.append(char)
steps = steps * 100
lines.pop(0)
lines.pop(0)
for line in lines:
    if line[2] == "A":
        bobs.append(line[:3])
for i, line in enumerate(lines):
    dict[line[:3]] = line[6:]
print(bobs)
for bob in bobs:
    count = 0
    while bob[-1] != "Z":
        for key in dict:
            left = dict[key][1:4]
            right = dict[key][6:9]
            if bob == key:
                if steps[count] == "L":
                    bob = left
                    count += 1
                    # print(str(count) + ": left : " + left)
                    # print("="*80)
                elif steps[count] == "R":
                    bob = right
                    count += 1
                    # print(str(count) + ": right :" +right)
                    # print("="*80)
            if bob[-1] == "Z":
                break
    print(bob)
    print(count)
    lol.append(count)
print(math.lcm(*lol))
print("Took", time.time() - start_time, "to run")
