import numpy as np

def galaxies():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    data = np.array([[galaxy == "#" for galaxy in line] for line in data])

    rows = []
    columns = []
    for index in range(len(data)):
        if not any(data[index, :]):
            rows.append(index)

        if not any(data[:, index]):
            columns.append(index)

    locations = np.where(data)
    locations = list(zip(locations[0], locations[1]))

    total1 = 0
    total2 = 0
    while locations:
        galaxy = locations.pop(0)

        for target in locations:
            distance = (abs(galaxy[0] - target[0]) + abs(galaxy[1] - target[1]))

            total1 += distance
            total2 += distance

            row_range = range(min(galaxy[0], target[0]), max(galaxy[0], target[0]))
            for row in rows:
                if row in row_range:
                    total1 += 1
                    total2 += 999999

            column_range = range(min(galaxy[1], target[1]), max(galaxy[1], target[1]))
            for column in columns:
                if column in column_range:
                    total1 += 1
                    total2 += 999999

    print(f"Total distances between galaxies part 1: {total1}")
    print(f"Total distances between galaxies part 2: {total2}")



if __name__ == "__main__":
    galaxies()



    