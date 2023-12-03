def navigation():

    with open("../input.txt", "r") as file:
        data = file.read().split(", ")

    coordinates = {
        "x": 0,
        "y": 0
    }

    directions = {
        0: ("y", 1), # North
        1: ("x", 1), # East
        2: ("y", -1), # South
        3: ("x", -1) # West
    }

    heading = 0
    locations = []
    first = None

    for instruction in data:

        if instruction[0] == "R":
            heading += 1
            if heading > 3: heading = 0

        else:
            heading -= 1
            if heading < 0: heading = 3

        steps = int(instruction[1:])
        axis, modifier = directions[heading]

        for _ in range(steps):
            coordinates[axis] += modifier
            location = f"{coordinates['x']}, {coordinates['y']}"

            if not first:
                if location in locations:
                    first = abs(coordinates["x"]) + abs(coordinates["y"])
                    continue

                locations.append(location)

    distance = abs(coordinates["x"]) + abs(coordinates["y"])

    print(f"Blocks away from Easter Bunny HQ: {distance}")
    print(f"Blocks away of first location visited twice: {first}")

if __name__ == "__main__":
    navigation()