def lights():
    with open("../input.txt", "r") as file:
        instructions = file.read().splitlines()

    grid = [[False for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        parts = instruction.split(" ")

        start_x, start_y = [int(number) for number in parts[-3].split(",")]
        stop_x, stop_y = [int(number) + 1 for number in parts[-1].split(",")]

        match parts[1]:
            case "on":
                switch = lambda x: True

            case "off":
                switch = lambda x: False

            case _:
                switch = lambda x: not x

        for x in range(start_x, stop_x):
            for y in range(start_y, stop_y):
                grid[y][x] = switch(grid[y][x])

    print(f"Lights on: {sum(sum(row) for row in grid)}")

if __name__ == "__main__":
    lights()