import json
from copy import deepcopy
from itertools import zip_longest

def distress():

    with open("../input.txt", "r") as file:
        lines = file.read().splitlines()

    ordered = 0
    signals = [
        [[2]],
        [[6]]
    ]

    for i in range(0,len(lines),3):
        left = json.loads(lines[i])
        right = json.loads(lines[i + 1])
        signals.append(left)
        signals.append(right)

        order = recursion(deepcopy(left), deepcopy(right))

        if order:
            ordered += i // 3 + 1

    print(f"Distress signals in order: {ordered}")

    length = len(signals)

    for i in range(length):
        for j in range(0, length - i - 1):
            order = recursion(deepcopy(signals[j]), deepcopy(signals[j + 1]))
            if not order:
                signals[j], signals[j + 1] = signals[j + 1], signals[j]

    dividers = [i + 1 for i in range(length) if signals[i] in [[[2]], [[6]]]]

    print(f"The decoder key is: {dividers[0] * dividers[1]}")

def recursion(left, right):

    if type(left) == type(right):
        types = type(left)

        if types == int:
            if left < right: return True
            elif left > right: return False
            return None
        
        if types == list:
            if not right and not left: return None
            if not left: return True
            if not right: return False

            for next_left, next_right in zip_longest(left, right, fillvalue=None):
                if next_left == None: return True
                if next_right == None: return False

                order = recursion(next_left, next_right)
                if order != None: return order

    else:
        if type(left) == int:
            order = recursion([left], right)
        else:
            order = recursion(left, [right])
        
        return order

if __name__ == "__main__":

    distress()