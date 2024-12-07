import numpy as np

def looper(matrix, start, orchestrator = False):
    x, y = start
    already_visited = []
    columns, rows = matrix.shape
    infinite_counter = 0
    rotation = 0

    while True:
        matrix[y][x] = "X"

        if (y - 1) not in range(rows):
            break

        if orchestrator and matrix[y - 1][x] == ".":
            new_matrix = matrix.copy()
            new_matrix[y - 1][x] = "#"
            infinite_counter += 1 if looper(new_matrix, (x, y)) == 0 else 0

        if matrix[y - 1][x] == "#":
            if (x, y, rotation) in already_visited:
                return 0
            
            already_visited.append((x, y, rotation))
            matrix = np.rot90(matrix)
            rotation += 1
            if rotation > 3: rotation = 0
            (x, y) = (y, columns - x - 1)
            continue

        y -= 1

    if orchestrator:
        return infinite_counter
        
    total = 0

    for row in matrix:
        for position in row:
            if position == "X":
                total += 1

    return total

def guard():
    with open("../input.txt", "r") as file:
        data = np.array([list(row) for row in file.read().splitlines()], dtype='U1')

    start = False

    for y, row in enumerate(data):
        for x, position in enumerate(row):
            if position == "^":
                start = (x, y)
                break

        if start:
            break

    positions = looper(data.copy(), start)
    infinite_loops = looper(data, start, True)

    print(f"Total of positions visited: {positions}")
    print(f"Total of infinite loops: {infinite_loops}")

if __name__ == "__main__":
    guard()