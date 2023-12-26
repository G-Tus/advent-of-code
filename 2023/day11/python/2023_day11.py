import numpy as np

def galaxies():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    data = np.array([[galaxy == "#" for galaxy in line] for line in data])

    for index in range(len(data) - 1, -1,  -1):
        row = data[index, :]
        if not any(row):
            data = np.insert(data, index, row, axis=0)

        column = data[:, index]
        if not any(column):
            data = np.insert(data, index, column, axis=1)

    locations = np.where(data)
    locations = list(zip(locations[0], locations[1]))

    total = 0
    while locations:
        galaxy = locations.pop(0)

        for target in locations:
            total += (abs(galaxy[0] - target[0]) + abs(galaxy[1] - target[1]))

    print(f"Total distances between galaxies: {total}")


if __name__ == "__main__":
    galaxies()



    