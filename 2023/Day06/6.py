d = open("6.in").read().strip()
lines = d.split("\n")
time = lines[0][5:].split()
distance = lines[1][9:].split()
ways = []
dict = {}
p1 = 1;
p2 = 0
for i, a in enumerate(time):
    count = 0
    starting = 0
    while starting < int(time[i]):
        if (starting * (int(time[i]) - starting) > int(distance[i])):
            count += 1
        starting += 1
    if count > 0:
        ways.append(count)

for a in ways:
    p1 *= a

def partTwo(t, d):
    count = 0
    for starting in range(t + 1):
        if (starting * (t - starting) > d):
            count += 1
    return count




print(ways) 
print(p1)
print(partTwo(55826490, 246144110121111))
