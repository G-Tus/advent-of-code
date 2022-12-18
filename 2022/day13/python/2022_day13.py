import json
from itertools import zip_longest

def distress():

    with open("../input.txt", "r") as file:
        lines = file.read().splitlines()

    ordered = 0

    for i in range(0,len(lines),3):
        left = json.loads(lines[i])
        right = json.loads(lines[i + 1])

        order = recursion(left, right)

        if order:
            ordered += i // 3 + 1

    print(ordered)

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