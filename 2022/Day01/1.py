d = open("1.in").read().strip()
lines = d.split("\n")
elfNum = 0
dict = {}
temp = 0
p1 = 0
p2 = 0
elves = [0]*248
for line in lines:
    if line == "":
        dict[elfNum] = temp
        elfNum += 1
        temp = 0
        continue
    temp += int(line)
for bob in dict:
    if (dict[bob] > p1):
        p1 = dict[bob]
        highestElf = bob
for i in range(248):
    elves[i] = dict[i]
elves.sort()
p1 = elves[-1]
p2 = elves[-1] + elves[-2] + elves[-3]
print(p1)
print(p2)

