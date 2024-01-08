import numpy as np
from copy import deepcopy

def lavafloor():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()
        data = [[space for space in row] for row in data]
        data = np.array(data)

    height = data.shape[0]
    width = data.shape[1]

    energized = np.full(data.shape, "", dtype="<U1")

    lasers = ["initial"]

    x = 0
    y = 0
    direction = "r"

    mirrors = {
        "\\": {
            "r": "d",
            "d": "r",
            "l": "u",
            "u": "l"
        },
        "/": {
            "r": "u",
            "d": "l",
            "l": "d",
            "u": "r"
        }
    }

    while lasers:

        energized[y, x] = direction

        match (space := data[y, x], direction):
            case ("-", "u" | "d"):
                lasers.append({
                    "x": x,
                    "y": y,
                    "direction": "l"
                })
                direction = "r"

            case ("|", "l" | "r"):
                lasers.append({
                    "x": x,
                    "y": y,
                    "direction": "u"
                })
                direction = "d"

            case ("\\" | "/", _):
                direction = mirrors[space][direction]

            case _:
                pass
  
        match direction:
            case "r":
                x += 1

            case "d":
                y += 1

            case "l":
                x -= 1

            case "u":
                y -= 1

        if x not in range(0, width) or y not in range(0, height) or energized[y, x] == direction:
            lasers.pop(0)

            if not lasers:
                break

            x, y, direction = lasers[0].values()

    print(f"Total tiles energized: {np.sum(energized != '')}")

if __name__ == "__main__":
    lavafloor()