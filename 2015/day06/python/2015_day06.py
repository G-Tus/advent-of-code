def lights():
    with open("../input.txt", "r") as file:
        instructions = file.read().splitlines()

    grid = [[False for _ in range(1000)] for _ in range(1000)]
    brightness = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        parts = instruction.split(" ")

        start_x, start_y = [int(number) for number in parts[-3].split(",")]
        stop_x, stop_y = [int(number) + 1 for number in parts[-1].split(",")]

        match parts[1]:
            case "on":
                switch = lambda _: True
                control = lambda x: x + 1

            case "off":
                switch = lambda _: False
                control = lambda x: 0 if x - 1 < 0 else x - 1

            case _:
                switch = lambda x: not x
                control = lambda x: x + 2

        for x in range(start_x, stop_x):
            for y in range(start_y, stop_y):
                grid[y][x] = switch(grid[y][x])
                brightness[y][x] = control(brightness[y][x])

    print(f"Lights on: {sum(sum(row) for row in grid)}")
    print(f"Total brightness: {sum(sum(row) for row in brightness)}")

if __name__ == "__main__":
    lights()