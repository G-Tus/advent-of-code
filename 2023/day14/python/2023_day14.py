import numpy as np

def roll_stones(data):

    height = len(data[:, 0])
    width = len(data[0, :])

    for y in range(height):
        for x in range(width):
            if data[y, x] != "O":
                continue

            for i in range(y, -1, -1):
                if i == 0 or data[i - 1, x] != ".":
                    break

                data[i, x] = "."
                data[i - 1, x] = "O"

    return data

def calculate_load(data):

    height = len(data[:, 0])
    width = len(data[0, :])

    total = 0

    for y in range(height):
        for x in range(width):
            if data[y, x] == "O":
                total += height - y

    return total

def reflector():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()
        data = [[character for character in line] for line in data]
        data = np.array(data)

    platform = roll_stones(data.copy())
    total = calculate_load(platform)

    print(f"Total load on north support beams: {total}")

    arrays = []
    done = False
    billion = 1000000000

    for i in range(1, billion + 1):
        for _ in range(4):
            data = roll_stones(data)
            data = np.rot90(data, k=-1)

        for j, array in enumerate(arrays, 1):
            if np.array_equal(array, data) and not ((billion - j) % (i - j)):
                done = True
                print(f"Repeating after {j} cycles, every {i - j} cycles, till {billion} cycles")
                break

        if done:
            break

        arrays.append(data.copy())

    total = calculate_load(data)
    print(f"Total load on north support beams after 1000000000 spin cycles: {total}")

if __name__ == "__main__":
    reflector()