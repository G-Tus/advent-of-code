import numpy as np

def forest():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    rows = len(data)
    columns = len(data[0])

    trees = np.empty((rows, columns), dtype=np.int8)
    visible = np.full((rows, columns), False, dtype=np.bool8)
    scenic = np.full((rows, columns), 1, dtype=np.int64)

    for i, row in enumerate(data):
        for j, column in enumerate(row):
            trees[i, j] = int(column)

    for _ in range(4):
        for i, row in enumerate(trees):
            highest = -1
            for j, column in enumerate(row):
                if column > highest:
                    highest = column
                    visible[i, j] = True

                count = 0
                for k in range(j + 1, columns):
                    count += 1
                    if row[k] >= column:
                        break

                scenic[i, j] *= count

        trees = np.rot90(trees, k=1, axes=(0, 1))
        visible = np.rot90(visible, k=1, axes=(0, 1))
        scenic = np.rot90(scenic, k=1, axes=(0, 1))

    print(f"Trees visible: {np.unique(visible, return_counts=True)[1][1]}")
    print(f"Max scenic score: {np.max(scenic)}")
    
if __name__ == "__main__":

    forest()