import numpy as np

def reflector():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()
        data = [[character for character in line] for line in data]
        data = np.array(data)

    height = len(data[:, 0])
    width = len(data[0, :])

    total = 0

    for y in range(height):
        for x in range(width):
            if data[y, x] != "O":
                continue

            for i in range(y, -1, -1):
                if i == 0 or data[i - 1, x] != ".":
                    break

                data[i, x] = "."
                data[i - 1, x] = "O"

            total += height - i

    print(f"Total load on north support beams: {total}")


if __name__ == "__main__":
    reflector()