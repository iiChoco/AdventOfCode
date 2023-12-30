import sys

d = open(sys.argv[1]).read().strip()

lines = d.split("\n")
grid = [[c for c in row] for row in lines]


def tilt(grid):
    temp = grid
    for i in range(len(temp)):
        for x, c in enumerate(temp[i]):
            if c == "O":
                if temp[i - 1][x] == ".":
                    print(temp[i - 1])
                    temp[i - 1][x] = "O"
                    print(temp[i - 1])
                    temp[i][x] = "."
    if temp == grid:
        print("Success")
        return temp
    else:
        print("Recursing")
        grid = temp
        return tilt(grid)


print(tilt(grid))
