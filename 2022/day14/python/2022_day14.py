import numpy as np

def sandcave():

    with open("../input.txt", "r") as file:
        rocks = file.read().splitlines()

    x_coordinates = []
    y_coordinates = []

    for rock in rocks:
        for pair in rock.split(" -> "):
            x, y = pair.split(",")
            x_coordinates.append(int(x))
            y_coordinates.append(int(y))

    min_x = min(x_coordinates) - 1
    max_x = max(x_coordinates) + 2
    max_y = max(y_coordinates) + 3

    offset = min_x
    width = max_x - min_x
    
    grid = np.full((max_y, width), False, dtype=np.bool8)
    grid[-1, :] = True

    for rock in rocks:
        pairs = rock.split(" -> ")
        start_x, start_y = [int(coordinate) for coordinate in pairs[0].split(",")]
        start_x -= offset

        for pair in pairs[1:]:
            end_x, end_y = [int(coordinate) for coordinate in pair.split(",")]
            end_x -= offset

            step_x = 1 if start_x <= end_x else -1
            step_y = 1 if start_y <= end_y else -1

            for x in range(start_x, end_x + step_x, step_x):
                for y in range(start_y, end_y + step_y, step_y):
                    grid[y, x] = True
            
            start_x, start_y = end_x, end_y

    column = [[False]] * max_y
    column[-1] = [True]

    part1 = False
    count = 0
    blocked = False
    while not blocked:
        rest = False
        x, y = 500 - offset, 0
        while not rest:

            if x == 0:
                grid = np.concatenate([column, grid], axis=1)
                offset -= 1

            if x == grid.shape[1] - 1:
                grid = np.concatenate([grid, column], axis=1)

            if y == max_y - 2 and not part1:
                part1 = True
                print(f"Units of sand at rest part 1: {count}")

            if not grid[y + 1, x]:
                y += 1
                continue

            if not grid[y + 1, x - 1]:
                y += 1
                x -= 1
                continue

            if not grid[y + 1, x + 1]:
                y += 1
                x += 1
                continue

            grid[y, x] = True
            count += 1
            rest = True

            if x == 500 - offset and y == 0:
                blocked = True

    print(f"Units of sand at rest part 2: {count}")

if __name__ == "__main__":

    sandcave()