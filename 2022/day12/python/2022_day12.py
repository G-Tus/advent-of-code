from queue import Queue
import numpy as np

def pathfinder():

    with open("../input.txt", "r") as file:
        grid = np.array([list(line) for line in file.read().splitlines()])

    rows, columns = grid.shape

    queue = Queue()
    nodes = []
    visited = []
    counts = {}

    begin_y, begin_x = [coordinate[0] for coordinate in np.where(grid == "S")]
    grid[begin_y, begin_x] = "a"
    begin = begin_y * columns + begin_x
    queue.put(begin)
    counts[begin] = 0

    end_y, end_x = [coordinate[0] for coordinate in np.where(grid == "E")]
    grid[end_y, end_x] = "z"
    end = end_y * columns + end_x

    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            neighbors = []

            for neighbor in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                y = i - neighbor[0]
                x = j - neighbor[1]

                if y not in range(rows) or x not in range(columns):
                    continue

                if ord(grid[y, x]) -  ord(column) < 2:
                    neighbors.append(y * columns + x)

            nodes.append(neighbors)

    while not queue.empty():
        node = queue.get(0)

        for neighbor in nodes[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.put(neighbor)
                counts[neighbor] = counts[node] + 1

    print(f"Steps from begin to end: {counts[end]}")

if __name__ == "__main__":

    pathfinder()
    
    

    
    


