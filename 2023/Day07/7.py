import sys

d = open(sys.argv[1]).read().strip()
lines = d.split("\n")

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

h = {}
cards = {
    "A": 0,
    "K": 0,
    "Q": 0,
    "J": 0,
    "T": 0,
    "9": 0,
    "8": 0,
    "7": 0,
    "6": 0,
    "5": 0,
    "4": 0,
    "3": 0,
    "2": 0,
}
five = []
high = []
onePair = []
twoPair = []
full = []
four = []
three = []

for line in lines:
    unique = 0
    hand, bet = line.split()
    h[hand] = bet
    pair_count = 0
    three_of_a_kind = False
    four_of_a_kind = False
    for ch in hand:
        for key in cards:
            if key == ch:
                cards[key] += 1
    for key in cards:
        if cards[key] == 1:
            unique += 1
        if cards[key] == 2:
            pair_count += 1
        if cards[key] == 3:
            three_of_a_kind = True
        if cards[key] == 4:
            four_of_a_kind = True
        if cards[key] == 5:
            five.append(line)
            print(key, pair_count)
    if unique == 5:
        high.append(line)
    elif three_of_a_kind and pair_count == 1:
        full.append(line)
    elif pair_count == 1:
        onePair.append(line)
    elif pair_count == 2:
        twoPair.append(line)
    elif four_of_a_kind:
        four.append(line)
    elif three_of_a_kind:
        three.append(line)

print(five)
print(high)
print(onePair)
print(twoPair)
print(three)
print(full)
print(five)
