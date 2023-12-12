d = open("4.in").read().strip()
lines = d.split('\n')
p1 = 0
p2 = 0
dict = {} 
for i in range(194):
    dict.update({i + 1:1})
for id, line in enumerate(lines):
    id += 1
    line = line[8:]
    winning, given = line.split(" | ")
    winning = winning.split()
    given = given.split()
    count = 0
    for a in given:
        for b in winning:
            if a == b:
                count += 1
    if (count > 0):
        p1 += 2**(count-1)   
    for i in range(count):
        for j in range(dict[id]):
            dict[id+i+1] += 1

for i in range(194):
    p2 += dict[i+1]
print("p1 = " + str(p1))
print("p2 = " + str(p2))
