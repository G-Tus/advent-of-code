from copy import deepcopy

START = (0, 0)

def presents():
    with open("../input.txt", "r") as file:
        data = file.read()

    house = deepcopy(START)
    houses = [house]

    for step in data:
        house = move(step, house)
        
        if house not in houses:
            houses.append(house)

    print(f"Houses with presents: {len(houses)}")

    santa = deepcopy(START)
    robo = deepcopy(START)
    houses = [santa]

    for i in range(0, len(data), 2):
        santa = move(data[i], santa)
        robo = move(data[i + 1], robo)

        if santa not in houses:
            houses.append(santa)

        if robo not in houses:
            houses.append(robo)

    print(f"Houses with presents teamwork: {len(houses)}")

def move(step, position):
    x, y = position
    match step:
        case "<":
            x -= 1
        
        case "^":
            y += 1

        case ">":
            x += 1

        case "v":
            y -= 1

    return (x, y)

if __name__ == "__main__":
    presents()