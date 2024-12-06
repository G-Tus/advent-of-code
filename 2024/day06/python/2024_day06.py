import numpy as np

def speed():
    with open("../input.txt", "r") as file:
        data = np.array([list(row) for row in file.read().splitlines()], dtype='U1')

    columns, rows = data.shape
    start = False

    for y, row in enumerate(data):
        for x, position in enumerate(row):
            if position == "^":
                start = True
                break

        if start:
            break

    while True:
        data[y][x] = "X"
        print(data)

        if (y - 1) not in range(rows):
            break

        if data[y - 1][x] == "#":
            data = np.rot90(data)
            (x, y) = (y, columns - x - 1)
            continue

        y -= 1

    total = 0

    for row in data:
        for position in row:
            if position == "X":
                total += 1

    print(f"Total of positions visited: {total}")

if __name__ == "__main__":
    speed()