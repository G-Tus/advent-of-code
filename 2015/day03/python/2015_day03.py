def presents():
    with open("../input.txt", "r") as file:
        data = file.read()

    x = 0
    y = 0

    houses = [(x, y)]

    for step in data:
        match step:
            case "<":
                x -= 1
            
            case "^":
                y += 1

            case ">":
                x += 1

            case "v":
                y -= 1

        if (house := (x, y)) not in houses:
            houses.append(house)

    print(f"Houses with presents: {len(houses)}")

if __name__ == "__main__":
    presents()