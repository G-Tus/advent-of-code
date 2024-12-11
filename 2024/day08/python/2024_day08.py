import numpy as np

def add_antinode(antinode, data):
    if (antinode >= 0).all() and (antinode < data.shape).all():
        data[tuple(antinode)] = "#"
        return True
    
    return False

def resonant_collinearity():
    with open("../input.txt", "r") as file:
        data = np.array([list(row) for row in file.read().splitlines()])

    frequencies = {}

    for y, row in enumerate(data):
        for x, antenna in enumerate(row):
            if antenna == ".":
                continue

            vector = np.array([y, x])

            if antenna not in frequencies:
                frequencies[antenna] = [vector]

            else:
                frequencies[antenna].append(vector)

    antinodes = np.full(data.shape, ".", dtype="U1")

    for antennas in frequencies.values():
        while antennas:
            antenna1 = antennas.pop(0)
            add_antinode(antenna1, antinodes)

            for antenna2 in antennas:
                add_antinode(antenna1 + (antenna1 - antenna2), data)
                add_antinode(antenna2 + (antenna2 - antenna1), data)

                i = 1
                while any((add_antinode(antenna1 + ((antenna1 - antenna2) * i), antinodes),
                           add_antinode(antenna2 + ((antenna2 - antenna1) * i), antinodes))):
                    i += 1

    print(f"Total amount of antinodes: {np.sum(data == '#')}")
    print(f"Total amount of antinodes part 2: {np.sum(antinodes == '#')}")

if __name__ == "__main__":
    resonant_collinearity()
