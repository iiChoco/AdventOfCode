d = open("2.in").read().strip()
lines = d.split("\n")
score = 0

for i, line in enumerate(lines):
    print(line)
    if (line[0] == "A" and line[-1] == "X"):
        score += 3
    if (line[0] == "B" and line[-1] == "Y"):
        score += 3
    if (line[0] == "C" and line[-1] == "Z"):
        score += 3
    if (line[0] == "A" and line[-1] == "Y"):
        score += 6
    if (line[0] == "B" and line[-1] == "Z"):
        score += 6
    if (line[0] == "C" and line[-1] == "X"):
        score += 6
    if (line[-1] == "X"):
        score += 1
    if (line[-1] == "Y"):
        score += 2
    if (line[-1] == "Z"):
        score += 3
    print ("Iteration #" + str(i))
    print(score)
    print("="*80)
print(score)
