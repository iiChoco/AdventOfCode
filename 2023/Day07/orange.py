import sys

f = open(sys.argv[1], "r")

lines = f.readlines()

entire = []
all_diff = []
one_p = []
two_p = []
three = []
four = []
five = []
full_house = []

card_val = {}


def convert(x):
    new = ""
    for i in x:
        if not i.isnumeric():
            if i == "T":
                new += "10"
            elif i == "J":
                new += "11"
            elif i == "Q":
                new += "12"
            elif i == "K":
                new += "13"
            elif i == "A":
                new += "14"
        else:
            new += i
    return int(new)


def Lconvert(x):
    new = []
    for i in x:
        if not i.isnumeric():
            if i == "T":
                new.append(10)
            elif i == "J":
                new.append(11)
            elif i == "Q":
                new.append(12)
            elif i == "K":
                new.append(13)
            elif i == "A":
                new.append(14)
        else:
            new.append(int(i))
    return new


for i in range(len(lines)):
    line = lines[i].strip("\n").split()

    savedhand = convert(line[0])
    bid = int(line[1])
    card_val[savedhand] = bid

    cards = Lconvert(list(line[0]))
    distinct = set(cards)
    length = len(distinct)
    if length == 1:
        five.append(cards)
    elif length == 2:
        max_count = 0
        for k in distinct:
            count = 0
            for p in cards:
                if k == p:
                    count += 1
            max_count = max(count, max_count)
        if max_count == 4:
            four.append(cards)
        else:
            full_house.append(cards)
    elif length == 3:
        max_count = 0
        for k in distinct:
            count = 0
            for p in cards:
                if k == p:
                    count += 1
            max_count = max(count, max_count)

        if max_count == 3:
            three.append(cards)
        else:
            two_p.append(cards)
    elif length == 4:
        one_p.append(cards)
    else:
        all_diff.append(cards)

print(len(all_diff))
print(len(one_p))
print(len(two_p))
print(len(three))
print(len(four))
print(len(five))
print(len(full_house))

all_diff = sorted(all_diff)
one_p = sorted(one_p)
two_p = sorted(two_p)
three = sorted(three)
four = sorted(four)
five = sorted(five)
full_house = sorted(full_house)


# print(all_diff)
# print(one_p)
# print(two_p)
# print(three)
# print(four)
# print(five)
# print(full_house)


def toOG(l):
    new = []
    for i in range(len(l)):
        now = l[i]
        string = ""
        for j in range(len(now)):
            string += str(now[j])

        new.append(int(string))

    return new


all_diff = toOG(all_diff)
one_p = toOG(one_p)
two_p = toOG(two_p)
three = toOG(three)
four = toOG(four)
five = toOG(five)
full_house = toOG(full_house)


for a in all_diff:
    entire.append(a)
for b in one_p:
    entire.append(b)
for c in two_p:
    entire.append(c)
for d in three:
    entire.append(d)
for e in full_house:
    entire.append(e)
for f in four:
    entire.append(f)
for g in five:
    entire.append(g)

sum = 0

for i in range(len(lines)):
    sum += card_val[entire[i]] * (i + 1)
print(sum)
