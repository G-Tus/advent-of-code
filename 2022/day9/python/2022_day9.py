from copy import deepcopy

def ropebridge():

    with open("../input.txt", "r") as file:
        steps = file.read().splitlines()

    length = 10
    knots = []
    for _ in range(10):
        knots.append([0, 0])

    count = {1: 1, 9: 1}
    history = {1: [[0, 0]], 9: [[0, 0]]}

    for step in steps:
        move, amount = step.split()

        match move:
            case 'U':
                transform = [0, 1]
            case 'D':
                transform = [0, -1]
            case 'L':
                transform = [-1, 0]
            case 'R':
                transform = [1, 0]

        for _ in range(int(amount)):
            knots[0][0] += transform[0]
            knots[0][1] += transform[1]
            pass
            for index in range(1, length):
                
                previous = index - 1
                diff = [knots[previous][0] - knots[index][0], knots[previous][1] - knots[index][1]]
                if -2 not in diff and 2 not in diff:
                    continue
                for i, gap in enumerate(diff):
                    if abs(gap) == 2:
                        knots[index][i] += int(gap / 2)
                    elif abs(gap) == 1:
                        knots[index][i] += gap
                if index in count:
                    if knots[index] not in history[index]:
                        count[index] += 1
                        history[index].append(deepcopy(knots[index]))
    
    print(f"Positions visited by tail 1: {count[1]}")
    print(f"Positions visited by tail 9: {count[9]}")

if __name__ == "__main__":

    ropebridge()
