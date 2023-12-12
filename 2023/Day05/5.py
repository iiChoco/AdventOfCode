d = open("5.in").read().strip()
lines = d.split("\n")


seeds = lines[0][6:].split()
soil = lines[3:50]
fertilizer = lines[52:84]
water = lines[86:96]
light = lines[98:124]
temp = lines[126:152]
humid = lines[154:194]
loc = lines[196:237]


for i, xd in enumerate(soil):
    bob = xd.split()
    for j, seed in enumerate(seeds):
        if int(bob[1]) < int(seed) < int(bob[1]) + int(bob[2]):
            seed = int(seed) + abs(int(bob[1]) - int(bob[0])) + 1
            seeds[j] = seed

for i, xd in enumerate(fertilizer):
    bob = xd.split()
    for j, seed in enumerate(seeds):
        if int(bob[1]) < int(seed) < int(bob[1]) + int(bob[2]):
            seed = int(seed) + abs(int(bob[1]) - int(bob[0])) + 1
            seeds[j] = seed

for i, xd in enumerate(water):
    bob = xd.split()
    for j, seed in enumerate(seeds):
        if int(bob[1]) < int(seed) < int(bob[1]) + int(bob[2]):
            seed = int(seed) + abs(int(bob[1]) - int(bob[0])) + 1
            seeds[j] = seed

for i, xd in enumerate(light):
    bob = xd.split()
    for j, seed in enumerate(seeds):
        if int(bob[1]) < int(seed) < int(bob[1]) + int(bob[2]):
            seed = int(seed) + abs(int(bob[1]) - int(bob[0])) + 1
            seeds[j] = seed

for i, xd in enumerate(temp):
    bob = xd.split()
    for j, seed in enumerate(seeds):
        if int(bob[1]) < int(seed) < int(bob[1]) + int(bob[2]):
            seed = int(seed) + abs(int(bob[1]) - int(bob[0])) + 1
            seeds[j] = seed

for i, xd in enumerate(humid):
    bob = xd.split()
    for j, seed in enumerate(seeds):
        if int(bob[1]) < int(seed) < int(bob[1]) + int(bob[2]):
            seed = int(seed) + abs(int(bob[1]) - int(bob[0])) + 1
            seeds[j] = seed

for i, xd in enumerate(loc):
    bob = xd.split()
    for j, seed in enumerate(seeds):
        if int(bob[1]) < int(seed) < int(bob[0]) + int(bob[2]):
            seed = int(seed) + abs(int(bob[1]) - int(bob[0])) + 1
            seeds[j] = seed

seeds.sort()

print("=" * 80)
print("Seeds:")
print(seeds)
print("=" * 80)
print("Seed to Soil Map:")
print(soil)
print("=" * 80)
print("Soil to Fertilizer Map:")
print(fertilizer)
print("=" * 80)
print("Fertilizer to Water Map:")
print(water)
print("=" * 80)
print("Water to Light Map:")
print(light)
print("=" * 80)
print("Light to Temperature Map:")
print(temp)
print("=" * 80)
print("Temperature to Humidity Map:")
print(humid)
print("=" * 80)
print("Humidity to Location Map:")
print(loc)
print("=" * 80)
print(seeds)
print(seeds[0])
