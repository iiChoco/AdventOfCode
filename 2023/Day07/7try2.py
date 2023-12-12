import sys

d = open(sys.argv[1]).read().strip()
lines = d.split("\n")


five = []
four = []
full = []
three = []
twoPair = []
onePair = []
high = []


def checkType():
    for line in lines:
        bob = line[:5]
        unique = 0
        pair_count = 0
        three_of_a_kind = False
        four_of_a_kind = False

        # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
        my_dict = {
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
        for char in bob:
            for key in my_dict:
                if char == key:
                    my_dict[key] += 1

        for key in my_dict:
            if my_dict[key] == 1:
                unique += 1
            if my_dict[key] == 2:
                pair_count += 1
            if my_dict[key] == 3:
                three_of_a_kind = true
            if my_dict[key] == 4:
                four_of_a_kind = true
            if my_dict[key] == 5:
                five.append(line)

        if unique == 5:
            high.append(line)
        if pair_count == 1:
            onePair.append(line)
        if pair_count == 2:
            twoPair.append(line)
        if three_of_a_kind and pair_count == 1:
            full.append(line)
        if four_of_a_kind:
            four.append(line)
        if three_of_a_kind:
            three.append(line)


checkType()

print("Five:", str(len(five)))
print("Four:", str(len(four)))
print("Full:", str(len(full)))
print("Three:", str(len(three)))
print("Two Pair:", str(len(twoPair)))
print("One Pair:", str(len(onePair)))
print("High:", str(len(high)))
