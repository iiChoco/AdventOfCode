import sys

d = open(sys.argv[1]).read().strip()

lines = ["." * 142]
lines += d.split("\n")
for i, line in enumerate(lines):
    lines[i] = "." + lines[i] + "."
lines.append("." * 142)

print(lines)
