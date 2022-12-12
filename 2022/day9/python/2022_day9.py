from copy import deepcopy

def ropebridge():

    with open("../input.txt", "r") as file:
        steps = file.read().splitlines()

    head = [0, 0]
    tail = [0, 0]
    count = 1
    history = []

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
            previous = deepcopy(head)
            head[0] += transform[0]
            head[1] += transform[1]

            diff_x = head[0] - tail[0]
            diff_y = head[1] - tail[1]

            if diff_x > 1 or diff_x < -1 or diff_y > 1 or diff_y < -1:
                tail = deepcopy(previous)
                if tail not in history:
                    count += 1
                    history.append(tail)
    
    print(f"Positions visited by tail: {count}")

if __name__ == "__main__":

    ropebridge()
