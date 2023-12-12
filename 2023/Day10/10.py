from collections import deque 

import sys

d = open(sys.argv[1]).read().strip().splitlines()
for r, row in enumerate(d):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

seen = {(sr,sc)}
q = deque([(sr,sc)])

while q:
    r, c = q.popLeft()
    ch = lines[r][c]

    if r > 0 and ch in "S|JL" and lines[r-1][c] == "|7F" and (r-1,c) not in seen:
        seen.add((r-1,c))
        q.append((r-1,c))
    if r < len(lines) - 1 and ch
