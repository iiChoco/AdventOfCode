import sys
from collections import Counter

d = open(sys.argv[1]).read().strip()

lines = d.split("\n")

five = []
four = []
full = []
three = []
two = []
one = []
high = []
winnings = 0
hands = {}


def has_count(counter, start, target):
    if counter[start] == target:
        return True
    return False


def has_count2(counter, target):
    for count in counter:
        if counter[count] == target and count != "J":
            return True
    return False


def checkHands2(hand):
    card_counts = Counter(hand)
    # XXXXJ
    # XXXAJ
    # XXABJ
    # XABJJ
    # KTJJT
    print(card_counts)
    if "J" in hand:
        highest = max(
            (card for card in card_counts if card != "J"),
            key=card_counts.get,
            default=None,
        )
        card_counts[highest] += card_counts["J"]
        assert card_counts["J"] != 0
        card_counts["J"] = 0
    print(card_counts)
    pairs = sum(1 for count in card_counts.values() if count == 2)
    threes = sum(1 for count in card_counts.values() if count == 3)
    fours = sum(1 for count in card_counts.values() if count == 4)

    if 5 in card_counts.values():
        five.append(hand)
    elif fours:
        four.append(hand)
    elif threes and pairs:
        full.append(hand)
    elif threes:
        three.append(hand)
    elif pairs == 2:
        two.append(hand)
    elif pairs == 1:
        one.append(hand)
    else:
        high.append(hand)


def checkHands(hand):
    card_counts = Counter(hand)

    pairs = sum(1 for count in card_counts.values() if count == 2)
    threes = sum(1 for count in card_counts.values() if count == 3)
    fours = sum(1 for count in card_counts.values() if count == 4)

    if 5 in card_counts.values():
        five.append(hand)
    elif fours:
        four.append(hand)
    elif threes and pairs:
        full.append(hand)
    elif threes:
        three.append(hand)
    elif pairs == 2:
        two.append(hand)
    elif pairs == 1:
        one.append(hand)
    else:
        high.append(hand)


# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
# A, B, C, D, E, F, G, H, I, J, K, L, or M
replace = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "P",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "L",
    "4": "M",
    "3": "N",
    "2": "O",
}


def sortHand(x):
    for i, hand in enumerate(x):
        for key in replace:
            hand = hand.replace(key, replace[key])
        x[i] = hand
    x.sort(reverse=True)
    for i, hand in enumerate(x):
        for key in replace:
            hand = hand.replace(replace[key], key)
        x[i] = hand


for line in lines:
    hand, bid = line.split()
    hands[hand] = bid
    checkHands2(hand)
sortHand(five)
sortHand(four)
sortHand(three)
sortHand(full)
sortHand(two)
sortHand(one)
sortHand(high)

all = []
for a in high:
    all.append(a)
for a in one:
    all.append(a)
for a in two:
    all.append(a)
for a in three:
    all.append(a)
for a in full:
    all.append(a)
for a in four:
    all.append(a)
for a in five:
    all.append(a)
print(all)
for a, i in enumerate(all):
    winnings += int(hands[i]) * (a + 1)
print(winnings)
