import sys

d = open(sys.argv[1]).read().strip()

patterns = d.split("\n\n")

for pattern in patterns:
    line = pattern.split('\n')
    length = len(line)
    for i in range(length):
        if line[i] == line[lenth - i]:


